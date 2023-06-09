import csv
from user import Customer

def writeToCSV(path, customer: Customer):
    file = open(path,'a')
    writer = csv.writer(file)
    row = (customer.name,customer.surname,customer.email, customer.age, customer.riskTag)
    writer.writerow(row)
    file.close()