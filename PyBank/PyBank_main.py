# PYBANK 
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os 
import csv

# Identify file and make it an object
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_profits_losses = 0
value = 0 
change_profits_losses = 0
dates = []
profits = []

# Open and read the file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
        
    # Read header row
    csv_header = next(csvreader)

    # Read first row
    first_row = next(csvreader)
    total_months += 1 
    total_profits_losses = int(first_row[1])
    value = int(first_row[1])

    # Loop through each row 
    for row in csvreader:
        # Keep track of dates
        dates.append(row[0]) 
        # Track changes  
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        # Total number of months 
        total_months += 1 

        # Total amount of Profit/Losses over the entire period 
        total_profits_losses = total_profits_losses + int(row[1])

    # Average of the changes in Profit/Losses over the entire period
    average_change = sum(profits)/len(profits)
    
    # Greatest increase in profits 
    greatest_profit_increase = max(profits)
    greatest_index = profits.index(greatest_profit_increase)
    greatest_date = dates[greatest_index]

    # Greatest decrease in profits 
    greatest_profit_decrease = min(profits)
    lowest_index = profits.index(greatest_profit_decrease)
    lowest_date = dates[lowest_index]

    # Change date format from MMM-YY to MMM-YYYY
    from datetime import datetime 
    greatest_date = datetime.strptime(greatest_date, "%b-%y").strftime('%b-%Y')
    lowest_date = datetime.strptime(lowest_date, "%b-%y").strftime('%b-%Y')

# Display information 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profits_losses)}")
print(f"Average Change in Profits: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_profit_increase)})")
print(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_profit_decrease)})")

# Export the text tile 
output = open("PyBank_text.txt","w")

line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profits_losses)}")
line5 = str(f"Average Change in Profits: ${str(round(average_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_profit_increase)})")
line7 = str(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_profit_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))


