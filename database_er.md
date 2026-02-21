
<img width="1711" height="1172" alt="image" src="https://github.com/user-attachments/assets/aecc0057-b0c0-4929-acd6-290fce8ce735" />

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




