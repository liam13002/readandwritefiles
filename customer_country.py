import csv

infile = open('customers.csv', 'r')

csvfile =csv.reader(infile, delimiter=',')

outfile = open("customer_country.csv", 'w')

next(csvfile)

outfile.write("Full Name, Country\n")

for record in csvfile:
    
    full_name = record[1] + " " + record[2]
    country = record[4]

    outfile.write(full_name + "," + country + "\n")

outfile.close()



