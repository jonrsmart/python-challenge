# Import dependencies
import os
import csv
import collections

#Define paths to data and output files
newtxt = os.path.join("analysis", "polling-results.txt")
csvpath = os.path.join("Resources", "election_data.csv")

#Define variables
total_votes = 0
#Use collections module to store candidates & votes received.
candidate_votes = collections.Counter()

#Open CSV and read file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first 
    csv_header = next(csvreader)
    #Read CSV rows
    for row in csvreader:
        #Running total of total votes
        total_votes += 1
        #Take the "Candidate" column, add name to dictionary as Key and then add 1 to value each time name appears. 
        candidate_votes[row[2]] += 1

#Sorted will sort the dictionary based on the values in the dictionary. Lambda allows us to define which item to sort by (votes in this case)
#As seen at: https://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/ 
#dict returns the tuples as a new dictionary
candidate_votes_sort = dict(sorted(candidate_votes.items(), key=lambda kv: kv[1], reverse=True))

#Split sorted dictionary into two lists of candidates and votes per candidate
candidates = list(candidate_votes_sort.keys())
votes_per = list(candidate_votes_sort.values())

#Define winner as the candidate in the first position
winner = candidates[0]

#Print Results
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes:,}')
print(f'-------------------------')
for x in range (0, len(candidates)):
    print(f'{candidates[x]}: {votes_per[x]/total_votes:.2%} ({votes_per[x]:,})')
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

#Output results to new TXT file
with open(newtxt, 'w', newline="") as writer:
    writer.write(f'Election Results\n')
    writer.write(f'-------------------------\n')
    writer.write(f'Total Votes: {total_votes:,}\n')
    writer.write(f'-------------------------\n')
    for x in range (0, len(candidates)):
        writer.write(f'{candidates[x]}: {votes_per[x]/total_votes:.2%} ({votes_per[x]:,})\n')
    writer.write(f'-------------------------\n')
    writer.write(f'Winner: {winner}\n')
    writer.write(f'-------------------------\n')

