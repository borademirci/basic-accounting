class Customer:
    def __init__(self, name, surname, email,age, income, loan): #constructor
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.income = income
        self.loan = loan
        self.riskTag = ""
        
    def isValidUser(self):
        if self.name.isalpha() == False or self.surname.isalpha() == False or self.age.isnumeric() == False or self.income.isnumeric() == False or self.loan.isnumeric() == False or self.isValidEmail() == False:
            return False
        return True
            
    def isValidEmail(self):
        email = self.email.strip().lower()
        if not "@" in email:
            return False
        elif not email[-4:] in ".com.org.edu.gov.net":
            return False
        return True
        
    def calculateBalance(self):
        self.calculateUserRisk()
        return int(self.income) - int(self.loan)
    
    def calculateUserRisk(self):
        if self.income > self.loan:
            self.riskTag = "Not Risky"
        else:
            self.riskTag = "Risky"

 