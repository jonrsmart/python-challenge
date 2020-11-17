# First we’ll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#Module for Counter function
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

candidate_votes_sort = dict(sorted(candidate_votes.items(), key=lambda keyvalue: keyvalue[1], reverse=True))
candidates = list(candidate_votes_sort.keys())
votes_per = list(candidate_votes_sort.values())
winner = candidates[0]

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes:,}')
print(f'-------------------------')
for x in range (0, len(candidates)):
    print(f'{candidates[x]}: {votes_per[x]/total_votes:.2%} ({votes_per[x]:,})')
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

