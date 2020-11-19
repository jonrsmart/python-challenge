#Import Dependencies
import os
import csv

#Define paths for data and output file
newtxt = os.path.join("analysis","profits.txt")
csvpath = os.path.join("Resources", "budget_data.csv")

#Define variables and lists for use below
net_profit = 0
profits = []
date = []
total_months = 0
monthly_change = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first 
    csv_header = next(csvreader)
    
    #Read each row in the CSV
    for row in csvreader:
        #Define revenue 
        revenue = int(row[1])
        
        #Count total months 
        total_months += 1
        
        #Track running net profit by adding each month's revenue to total
        net_profit += revenue
        
        #Add each months revenue to profits list
        profits.append(revenue)
        
        #Add date to date list
        date.append(row[0])

#Calculating average change by looping through profits list
for i in range(1,len(profits)):
    #subtract next item in list from current item in list and then save value to monthly_change list
    monthly_change.append(profits[i] - profits[i-1])
#calculate average monthly change
average_change = sum(monthly_change) / len(monthly_change)  

#Determine greatest increase and greatest decrease

#Max and Min to determine values of greatest increase and greatest decrease
maxprofit = max(profits)
maxloss = min(profits)

#Taking index position of Max and Min in the profit list, finding same index in the date list and saving value as variable
maxprofdate = date[profits.index(maxprofit)]
maxlossdate = date[profits.index(maxloss)]

#Print results with number formatting applied
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_profit:,}')
print(f'Average Change: ${average_change:+.2f}')
print(f'Greatest Increase in Profits: {maxprofdate} ({maxprofit:,})')
print(f'Greatest Decrease in Profits: {maxlossdate} ({maxloss:,})')

#Output results to new TXT file in "output" folder
with open(newtxt, 'w', newline="") as writer:
    writer.write(f'Financial Analysis\n')
    writer.write(f'----------------------------\n')
    writer.write(f'Total Months: {total_months}\n')
    writer.write(f'Total: ${net_profit:,}\n')
    writer.write(f'Average Change: ${average_change:+.2f}\n')
    writer.write(f'Greatest Increase in Profits: {maxprofdate} ({maxprofit:,})\n')
    writer.write(f'Greatest Decrease in Profits: {maxlossdate} ({maxloss:,})\n')
  
        