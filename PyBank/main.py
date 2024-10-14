# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
max_profit = 0
min_profit = 0
net_change_list = []
previous_net = 0
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    previous_net = float(first_row[1])
    #print(previous_net)

    # Track the total and net change
    total_months += 1
    total_net += previous_net

    # Process each row of data
    for row in reader:

        month = row[0]
        net = float(row[1])
        
        # Track the total
        total_months += 1
        
        # Track the net change
        total_net += net

        if previous_net != 0:
            net_change = net - previous_net
            net_change_list.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
            if net_change > max_profit:
                max_profit = net_change
                max_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
            if net_change < min_profit:
                min_profit = net_change
                min_month = row[0]

        previous_net = net

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary

output = ("Financial Analysis\n"
         "------------------------------\n"
         f'Total Months: {total_months}\n'
         f'Total: ${total_net:0.0f}\n'
         f'Average Change: ${average_change:0.2f}\n'
         f'Greatest Increase in Profit: {max_month} (${max_profit:0.0f})\n'
         f'Greatest Decrease in Profits: {min_month} (${min_profit:0.0f})\n')

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
