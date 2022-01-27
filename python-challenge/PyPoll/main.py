===========================================================================
#You will be give a set of poll data called election_data.csv. The dataset is 
#composed of three columns: Voter ID, County, and Candidate. Your task is to 
#create a Python script that analyzes the votes and calculates each of the following:
#
#The total number of votes cast
#
#A complete list of candidates who received votes
#
#The percentage of votes each candidate won
#
#The total number of votes each candidate won
#
#The winner of the election based on popular vote.
#
#As an example, your analysis should look similar to the one below:
#
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
#
#NOTE TO SELF:  DON'T EVER USE THE SAME NAME IN DIFFERENT FOR LOOPS! 
#               (NO -->   a) for ROW in range, b) for ROW in range)
#               (YES -->  a) for ROW in range, b) for Y in range etc..)
#               IF VARIABLES ARE IN BOTH LOOPS, YOU JUST F*CKED YOURSELF!!
#===========================================================================
import os
import csv

# path to data file
budget_data_csv = os.path.join('election_data.csv')

#variables
total_votes = 0
candidates_unique = []
candidate_vote_count = []

#read the csv file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #This is the total votes cast, just count rows
        total_votes += 1
        #read in the candidate from column 3 of csv
        candidate_in = (row[2])
        #if candidate alreaady in list then locate the candidate by index # and increment the vote count by 1
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            #if candidate was not found in candidates_unique list then append to list and add 1 to vote count
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)

#----------------------------------------------------
#QA the variables
#print(f'Total votes {total_votes}')
#print(f'Each candidate: {candidates_unique}')
#print(f'Index: {candidates_unique.index(candidate_in)}')
#----------------------------------------------------

pct = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
    #calculation to get the percentage, x is the looper value
    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index] 

#----------------------------------------------------
#QA the variables
#print(f'Vote count for each candidate: {candidate_vote_count}')
#print(f'Max votes: {max_votes}')
#print(f'Election winner: {election_winner}')
#----------------------------------------------------

#To terminal
print('======================================================')
print('|                  Election Results                  |')
print('======================================================')
print(f'Total Votes: {total_votes}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Election winner: {election_winner.upper()}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


#output txt file
output_file = os.path.join("pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('======================================================\n')
    datafile.write('|                  Election Results                  |\n')
    datafile.write('======================================================\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    for x in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write("---END OF REPORT---")
