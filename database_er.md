
<img width="743" height="1207" alt="Screenshot 2026-04-01 222631" src="https://github.com/user-attachments/assets/b38de028-a013-45c1-ae1d-754d116ab362" />

Entities
Strong: Customer, LoanApp, Loan, Risk
Weak: LoanPayment
Associative: LoanApp

Relationships
One to One: Loan - Risk
One to Many: Customer - LoanApp
One to Many: Loan - LoanPayment
Many to Many: none

Attributes
Identifier: CUSTID, LOAN_APP_ID, LOANID
Mandatory: GENDER, MARRIED, EDUCATION, INCOME, CREDIT_SCORE, LOAN_AMMOUNT, APPLICATION_DATE, APP_STATUS, APPROVED_AMOUNT, INTEREST_RATE, START_DATE, RISK_SCORE, APPROVE, PAYMENT_DATE, AMMOUNT_PAYED
Optional: none
Singlevalue: CREDIT_SCORE, RISK_SCORE, INTEREST_RATE, INCOME, LOAN_AMMOUNT, APPROVED_AMOUNT, AMMOUNT_PAYED


