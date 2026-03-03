
<img width="754" height="1053" alt="image" src="https://github.com/user-attachments/assets/629960e7-7149-41af-9aa7-6e9020639fb5" />

Entities
Strong: Customer, LoanOfficer, LoanProduct, RiskAssessment, Loan
Weak: LoanPayment 
Associative: LoanApplication 

Relationships
One to One: LoanApplication 
One to Many: Customer  
Many to Many: LoanProduct 

Attributes
Identifier: CustomerID, ApplicationID, LoanID, AssessmentID
Mandatory: FullName, RequestedAmount, ApplicationDate, PaymentDate, Status
Optional: Email, Notes, MiddleName
Singlevalue: CreditScore, RiskScore, InterestRate, PhoneNumber




