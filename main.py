from user import Customer
import writer
    




def main():
    print("Accounting service")
    customer1 = Customer(input("Please enter customer name:"),
                         input("Please enter customer surname:"),
                         input("Please enter customer email:"),
                         input("Please enter customer age:"),
                         input("Please enter customer income:"),
                         input("Please enter customer loan:"))
    
    if customer1.isValidUser() == False:
        print("Invalid user credential")
    else:
        print("User is valid")
        
    
    print("Customer total balance is:", customer1.calculateBalance())
    writer.writeToCSV("report.csv", customer1)
    
        
  
    
if __name__ == "__main__":
    main()