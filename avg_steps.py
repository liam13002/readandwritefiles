import csv
infile =open('steps.csv', 'r')
csvfile = csv.reader(infile, delimiter=',')
next(csvfile)
outfile =open("avg_steps.csv","w")

months = ['Dummy','January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']

days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

month = 1
total_steps = 0



for rec in csvfile:
    
   

    if rec[0] == str(month):
        total_steps+= int(rec[1])
    else:
        
        average = format((total_steps / days[month]), '.2f')
        outfile.write(months[month])
        outfile.write(', ')
        outfile.write(str(average))
        outfile.write('\n')
        month += 1
        total_steps = int(rec[1])
average = format((total_steps / days[month]), '.2f')
outfile.write(months[month])
outfile.write(', ')
outfile.write(str(average))
outfile.write('\n')



        
    
outfile.close()


