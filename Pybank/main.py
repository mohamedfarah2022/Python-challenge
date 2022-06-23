#insert os and csv to start script
import os
import csv

# Set path for file to work on
csvpath = os.path.join("..", "Resources", "budget_data.csv.csv")

#set variables concentrated on
months = []
profit_losses_list = []

change_sum = 0
greatest_increase_in_profit = 0
greatest_decrease_in_profit = 0

# Open the CSV excel sheet with path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # overlook headers of table of csv spreadsheet
    csv_header = next(csvreader)
    
    # Determine first row value
    first_row = next(csvreader)
    previousvalue = int(first_row[1])
    row_count = 1
    total = previousvalue

    # Read each row of data after the header
    for row in csvreader:
        # Determines the number of rows which equate to months
        row_count = row_count + 1

        # Determines the total profit/losses
        total = total + int(row[1])

        # Calculates the difference in change
        nextvalue = int(row[1])
        change = 0
        change = nextvalue - int(previousvalue)
        change_sum = change_sum + change
        previousvalue = int(row[1])
   
    #compare the profit to the change
        if change > greatest_increase_in_profit:
            greatest_increase_in_profit = change
            greatest_month = row[0]
        if change < greatest_decrease_in_profit:
            greatest_decrease_in_profit = change
            lowest_month = row[0]

    average_change = round((change_sum) / (row_count - 1), 2)

#print out the value gained from the script done with these lines
print("''text")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(total))
print("Average Change: $" + str(average_change))
print( f'Greatest Increase in Profits: {greatest_month} (${greatest_increase_in_profit})')
print(f'Greatest Decrease in Profits: {lowest_month} (${greatest_decrease_in_profit})')

#create .txt file for the outcome with a os linkage
output_file = os.path.join("pybank.txt")

#print lines on .txt file
with open(output_file, "w") as datafile:
    print("'''text", file=datafile)
    print("Financial Analysis", file=datafile)
    print("----------------------------", file=datafile)
    print("Total Months: " + str(row_count), file=datafile)
    print("Total: $" + str(total), file=datafile)
    print("Average Change: $" + str(average_change), file=datafile)
    print( f'Greatest Increase in Profits: {greatest_month} (${greatest_increase_in_profit})', file=datafile)
    print(f'Greatest Decrease in Profits: {lowest_month} (${greatest_decrease_in_profit})', file=datafile)