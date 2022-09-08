import csv

infile=open("steps.csv","r")
outfile=open("avg_steps.csv","w")

csvfile_old=csv.reader(infile, delimiter=',')
csvfile_new=csv.reader(outfile, delimiter=',')

csvinput=csv.writer(outfile)

infile.readline()

num_days=0

total_steps=0

for record in csvfile_old:
    steps=int(record[1])

    if record[0]=="1":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps1=total_steps/num_days

        

    if record[0]=="2":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps2=total_steps/num_days
    
    if record[0]=="3":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps3=total_steps/num_days
    
    if record[0]=="4":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps4=total_steps/num_days

    if record[0]=="5":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps5=total_steps/num_days
    
    if record[0]=="6":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps6=total_steps/num_days
    
    if record[0]=="7":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps7=total_steps/num_days

    if record[0]=="8":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps8=total_steps/num_days

    if record[0]=="9":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps9=total_steps/num_days

    if record[0]=="10":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps10=total_steps/num_days
    
    if record[0]=="11":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps11=total_steps/num_days
    
    if record[0]=="12":
        num_days+=record.count(record[0])
        total_steps+=steps
        avg_steps12=total_steps/num_days

csvinput.writerow(["January",avg_steps1])
csvinput.writerow(["February",avg_steps2])
csvinput.writerow(["March",avg_steps3])
csvinput.writerow(["April",avg_steps4])
csvinput.writerow(["May",avg_steps5])
csvinput.writerow(["June",avg_steps6])
csvinput.writerow(["July",avg_steps7])
csvinput.writerow(["August",avg_steps8])
csvinput.writerow(["September",avg_steps9])
csvinput.writerow(["October",avg_steps10])
csvinput.writerow(["November",avg_steps11])
csvinput.writerow(["December",avg_steps12])


outfile.close()
