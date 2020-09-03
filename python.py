import os
import csv

#locate csv file in resources folder
csvpath = os.path.join("./Resources/budget_data.csv")

#create lists to store the data in
date = []
profit_loss = []

#read in the data and write it into the lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])

#calculate total number of months by counting number of rows in list
total_months = len(date)

#compounding all profits and losses in 'for' loop
total_profits = 0
for x in profit_loss:
    total_profits += int(x)

#avg change in profit/loss, loop through months and compare x+1 to x, add it all up and divide by number of months-1
prof=0
for x in range(total_months -1):
    prof = prof + int(profit_loss[x+1])-int(profit_loss[x])
avgprof=round(prof/(total_months-1),2)

#finding the biggest profit and loss
#set max and min to 0 to start
max=0
min=0
#loop through all the months
for x in range(total_months-1):
    #calculate profit for that month, call it 'newprofit'
    newprofit=int(profit_loss[x+1])-int(profit_loss[x])
    #if new profit exceeds old max, replace it
    if newprofit>max:
        max=newprofit
        #record month of newprofit
        bestmonth=date[x+1]
    #if loss is worse the current min, replace it
    if newprofit<min:
        min=newprofit
        #write out the month of loss
        worstmonth=date[x+1]

#print it all out
print(f"Financial Analysis")
print(f"--------------------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total_profits}")
print(f"Average Change: $ {avgprof}")
print(f"Greatest Increase in Profits: {bestmonth} (${max})")
print(f"Greatest Decrease in Profits: {worstmonth} (${min})")

#Let's write it into a file
#First, put this data into some lists

column_a = ["Financial Analysis", "-------", "Total Months", "Total: $", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"]
column_b = ["","",total_months,total_profits,avgprof,bestmonth,worstmonth]
column_c = ["","","","","",max,min]

#zip lists together
cleaned_csv = zip(column_a, column_b, column_c)

#set variable for output file
output_path = os.path.join("Financial_Analysis.csv")

#open output file
with open(output_path, "w") as csvfile:

    csvwriter = csv.writer(csvfile)
    
    #write zipped rows
    csvwriter.writerows(cleaned_csv)

    




