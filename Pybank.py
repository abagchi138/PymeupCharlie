import os
import csv


csvpath = os.path.join("budget_data.csv")

# List creation
totalmonths = []
total_profitlosses = []
change = []



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    header= next(csvreader)

    #to read the number of months
    for row in csvreader:
        totalmonths.append(row[0])
        total_profitlosses.append(int(row[1]))


    #to show change in profit and losses
    for i in range(len(total_profitlosses) - 1):
        change.append(total_profitlosses[i + 1] - total_profitlosses[i])


max_value = max(change)
max_month = change.index(max(change)) + 1

min_value = min(change)
min_month = change.index(min(change)) + 1

#printing all the values

print(f"Total Months: {len(totalmonths)}")
print(f"Total: ${sum (total_profitlosses)}")
print(f"Average Change: {round (sum(change) / len(change), 2)}")
print(f"Greatest Increase in Profits: {totalmonths[max_month]} : {(str(max_value ))}")
print(f"Greatest Decrease in Profits: {totalmonths[min_month]} : {(str(min_value ))}")