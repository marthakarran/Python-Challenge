#PYPOLL

# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

# Identify file and make it an object 
election_data = os.path.join("election_data.csv")

# Lists for names of candidates, number of votes per candidate, percentage of total votes per candidate 
candidates = []
candidate_votes = []
candidate_votes_percentage = []

# Counter for total number of votes 
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1
    
    # Add to candidate_votes_percentage list 
    for votes in candidate_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        candidate_votes_percentage.append(percentage)
    
    # Find winning candidate
    winner = max(candidate_votes)
    index = candidate_votes.index(winner)
    winning_candidate = candidates[index]

# Display results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")

for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(candidate_votes_percentage[i])} ({str(candidate_votes[i])})")

print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Export to text file
output = open("PyPoll_text.txt", "w")
line1 = "Election Results"
line2 = "-------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = "-------------------------"

output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))

for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(candidate_votes_percentage[i])} ({str(candidate_votes[i])})")
    output.write('{}\n'.format(line))

line5 = "-------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "-------------------------"

output.write('{}\n{}\n{}\n'.format(line5, line6, line7))

