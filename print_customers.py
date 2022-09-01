import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile) #skips first row
for record in csvfile:

        print("ID:", record[0])
        print("First name:", record[1])
        print("Last name:", record[2])
        print("City:", record[3])
        print("Country:", record[4])
        print("Phone:", record[5])
        input("Press enter for next customer:")

