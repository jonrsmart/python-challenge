# First we’ll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
newtxt = os.path.join("analysis","profits.txt")
csvpath = os.path.join("Resources", "budget_data.csv")
net_profit = 0
profits = []
date = []
total_months = 0
monthly_change = []

with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        revenue = int(row[1])
        total_months += 1
        net_profit += revenue
        profits.append(revenue)
        date.append(row[0])

for i in range(1,len(profits)):
    monthly_change.append(profits[i] - profits[i-1])
average_change = sum(monthly_change) / len(monthly_change)  

maxprofit = max(profits)
maxloss = min(profits)
maxprofdate = date[profits.index(maxprofit)]
maxlossdate = date[profits.index(maxloss)]

print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_profit:,}')
print(f'Average Change: ${average_change:+.2f}')
print(f'Greatest Increase in Profits: {maxprofdate} ({maxprofit:,})')
print(f'Greatest Decrease in Profits: {maxlossdate} ({maxloss:,})')



with open(newtxt, 'w', newline="") as writer:
    writer.write(f'Financial Analysis\n')
    writer.write(f'----------------------------\n')
    writer.write(f'Total Months: {total_months}\n')
    writer.write(f'Total: ${net_profit:,}\n')
    writer.write(f'Average Change: ${average_change:+.2f}\n')
    writer.write(f'Greatest Increase in Profits: {maxprofdate} ({maxprofit:,})\n')
    writer.write(f'Greatest Decrease in Profits: {maxlossdate} ({maxloss:,})\n')
  
        