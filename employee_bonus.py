import csv

infile = open('employeepay.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')




next(csvfile) #skips first row
for record in csvfile:

        pay = int(record[3])
        bonus = float(record[4])
        total_pay = pay + (bonus*pay)

        print("ID:", record[0])
        print("First name:", record[1])
        print("Last name:", record[2])
        print("Salary:", record[3])
        print("Bonus:", record[4])
        print("Total Pay:", total_pay)
        input("Press enter for next customer:")