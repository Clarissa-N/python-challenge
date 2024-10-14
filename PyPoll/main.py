# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
percent_votes = (0)
candidate_list = {}
results = ""
# Winning Candidate and Winning Count Tracker
winning_count = 0

winner = " "


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_list:
            candidate_list[candidate] = 0
            

        # Add a vote to the candidate's count
        candidate_list[candidate] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_list:
        candidate_votes = candidate_list[candidate]

        # Get the vote count and calculate the percentage
        percent_votes = (candidate_votes/total_votes) * 100

        # Update the winning candidate if this one has more votes
        if candidate_votes > winning_count:
            winning_count = candidate_votes
            winner = candidate
        
        candidate_list[candidate] = (percent_votes, candidate_votes)

        # Print and save each candidate's vote count and percentage
        results += (f"{candidate}: {percent_votes:0.03f}% ({candidate_votes})\n")

    # Generate and print the winning candidate summary
    output = ("Election Results\n"
             "------------------------------\n"
             f'Total Votes: {total_votes}\n'
             f'-----------------------------\n'
             f'{results}\n'
             f'Winner: {winner}\n')

    print(output)

    txt_file.write(output)
    # Save the winning candidate summary to the text file
