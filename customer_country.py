import csv

infile = open('customers.csv', 'r')

outfile =open('customer_country.csv', 'w')

count = 0

for line in infile:
    outfile.write(line[1])
   
    count = count + 1

print(count)

