import os
import csv

csvpath= os.path.join(budget_data.csv')

total_months=0
nettotal=0
changes= 0
great_increase= 0
great_decrease= 0

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimeter= ',')

    for row in csvreader:
        total_months +=1
        net_total += int(row[1])

changes= net_total / total_months
