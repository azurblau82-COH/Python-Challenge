import os
import csv

#locate csv file in resources folder
csvpath = os.path.join("./Resources/election_data.csv")

#create lists to store the data in
voter_ID = []
county = []
candidate = []

#read in the data and write it into the lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    csv_header = next(csvfile)
    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#total votes cast is length of list minus 1 for header
total_votes = len(voter_ID)




#set up a list to fill with candidates, vote talleys, and percentage of votes
findcandidates = []
numberofvotes = []
percentage =[]

#loop through list to find candidates
for x in range(total_votes):
    #if candidate not yet in list, add name, and create an entry for vote tally, starting at 0, create entry to calculate percentage
    if candidate[x] not in findcandidates:
        findcandidates.append(candidate[x])
        numberofvotes.append(0)
        percentage.append(0)
    #add a vote to the correct element in the list. first find element index, than add 1 vote
    vote = findcandidates.index(candidate[x])
    numberofvotes[vote]=int(numberofvotes[vote])+1

#calculate percentages
for x in range(len(percentage)):
    percentage[x] = (int(numberofvotes[x]) / total_votes) * 100

#the winner is the one with the most votes. 
#max returns most votes, find element, than find candidate for that element number (there may be a more elegant way, but hey...it works)
winner=findcandidates[numberofvotes.index(max(numberofvotes))]

#print out the results!
print(f"Election Results")
print(f"----------------")
print(f"Total Votes: {total_votes}")
for x in range(len(findcandidates)):
    print(f"Candidate: {findcandidates[x]} {round(percentage[x],3)}% ({numberofvotes[x]})")
print(f"----------------")
print(f"Winner: {winner}")
print(f"----------------")

#write out the results
#First, put this data into some lists
column_a = ["Election Results", "Total Votes:"]
column_b = ["",total_votes]
column_c = ["",""]

#add results for however many candidates are found
for x in range(len(findcandidates)):
    column_a.append(findcandidates[x])
    column_b.append(percentage[x])
    column_c.append(numberofvotes[x])

#add winner results
column_a.append("Winner:")
column_b.append(winner)
column_c.append("")

#zip lists together
cleaned_csv = zip(column_a, column_b, column_c)

#set variable for output file
output_path = os.path.join("./Analysis/Election_Results.csv")

#open output file
with open(output_path, "w") as csvfile:

    csvwriter = csv.writer(csvfile)
    
    #write zipped rows
    csvwriter.writerows(cleaned_csv)
