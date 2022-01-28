# Modules
import os
import csv

# Set path to file
csvpath = os.path.join("Resources", "election_data.csv")

#Set up Variables to count votes, both total and individual
vote_totals = 0
ind_candidate = []
candidate_total_votes = []

# Open the CSV 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row
    header = next(csvreader)

    for row in csvreader:
        candidate_in = (row[2])
        if candidate_in in ind_candidate:
            candidate_index = ind_candidate.index(candidate_in)
            candidate_total_votes[candidate_index] = candidate_total_votes[candidate_index] + 1
        else:
            ind_candidate.append(candidate_in)
    
    candidate_total_votes.append

# print(f'Total totavote}')
# print(f'Each candidate: {ind_candidate}')
# print(f'Index: {ind_candidate.index(candidate_in)}')


