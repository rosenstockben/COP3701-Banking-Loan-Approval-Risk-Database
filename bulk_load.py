import oracledb
import csv
import os

LIB_DIR = "C:\oracle\instantclient_21_3"
DB_USER = "ROSENSTOCKBEN_SCHEMA_LGH20"
DB_PASS = "VO3#F4ULJPMPEZZAMI1BI86OCX69x4"
DB_DSN  = "db.freesql.com:1521/23ai_34ui2"

oracledb.init_oracle_client(lib_dir=LIB_DIR)

def bulk_load_csv(file_path: str):
    try:
        filename = os.path.basename(file_path).upper()

        if "CUSTOMER" in filename:
            sql = """
                INSERT INTO CUSTOMER 
                (CUSTID, GENDER, MARRIED, EDUCATION, INCOME, CREDIT_SCORE) 
                VALUES (:1, :2, :3, :4, :5, :6)
            """
        elif "LOAN_APP" in filename:
            sql = """
                INSERT INTO LOAN_APP 
                (LOAN_APP_ID, CUSTID, LOAN_AMMOUNT, APPLICATION_DATE, APP_STATUS) 
                VALUES (:1, :2, :3, to_date(:4, 'mm/dd/yyyy'), :5)
            """
        elif "LOAN" in filename:
            sql = """
                INSERT INTO LOAN 
                (LOANID, LOAN_APP_ID, APPROVED_AMOUNT, INTEREST_RATE, START_DATE) 
                VALUES (:1, :2, :3, :4, to_date(:5, 'mm/dd/yyyy'))
            """
        elif "LOAN_PAYMENT" in filename:
            sql = """
                INSERT INTO LOAN_PAYMENT 
                (LOANID, PAYMENT_DATE, AMMOUNT_PAYED) 
                VALUES (:1, to_date(:2, 'mm/dd/yyyy'), :3)
            """
        elif "RISK" in filename:
            sql = """
                INSERT INTO RISK 
                (LOANID, RISK_SCORE, APPROVE) 
                VALUES (:1, :2, :3)
            """
        else:
            print(f" Unknown file: {file_path}")
            return

        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()

        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)                    # skip header
            data_to_insert = [row for row in reader]

        if not data_to_insert:
            print(f"  {file_path} is empty (after header).")
            return

        print(f" Loading {len(data_to_insert):,} rows from {os.path.basename(file_path)} ...")
        cursor.executemany(sql, data_to_insert)

        conn.commit()
        print(f" Successfully loaded {cursor.rowcount:,} rows into {filename.split('.')[0]}")

    except Exception as e:
        print(f" Error loading {file_path}: {e}")
        if 'conn' in locals():
            conn.rollback()
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


if __name__ == "__main__":
    csv_files = [
        r"data\CUSTOMER.csv",
        r"data\LOAN_APP.csv",
        r"data\LOAN.csv",
        r"data\LOAN_PAYMENT.csv",
        r"data\RISK.csv",
    ]

    for csv_file in csv_files:
        if os.path.exists(csv_file):
            bulk_load_csv(csv_file)
        else:
            print(f" File not found: {csv_file}")

    print("\n All files processed!") 