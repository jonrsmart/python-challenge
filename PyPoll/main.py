# First we’ll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
import collections

csvpath = os.path.join("Resources", "election_data.csv")
total_votes = 0
candidate_votes = collections.Counter()

with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate_votes[row[2]] += 1

candidate_votes_sort = dict(sorted(candidate_votes.items(), key=lambda kv: kv[1], reverse=True))
candidates = list(candidate_votes_sort.keys())
votes_per = list(candidate_votes_sort.values())
winner = candidates[0]

candidate1_perc = votes_per[0]/total_votes
candidate2_perc = votes_per[1]/total_votes
candidate3_perc = votes_per[2]/total_votes
candidate4_perc = votes_per[3]/total_votes


print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {candidate1_perc:.2%} ({votes_per[0]})')
print(f'Correy: {candidate2_perc:.2%} ({votes_per[1]})')
print(f'Li: {candidate3_perc:.2%} ({votes_per[2]})')
print(f"O'Tooley: {candidate4_perc:.2%} ({votes_per[3]})")
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')