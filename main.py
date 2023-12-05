import os
import csv

pollData = os.path.join("C:\Drake State Data Analyst\Challenges\python-challenge\PyPoll\Resources\election_data.csv")

with open(pollData) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    csv_header = next(csvreader)

    data = list(csvreader)
    row_count = len(data)

    candilist = list()
    tally = list()

for i  in range (0,row_count):
    candidate = data[i][2]
    tally.append(candidate)

    if candidate not in candilist:
        candilist.append(candidate)
candicount = len(candilist)

votes = list()
percentage = list()

for j in range (0, candicount):
    name = candilist[j]
    votes.append(tally.count(name))
    vprct = votes[j]/row_count
    percentage.append(vprct)

winner = votes.index(max(votes))

print("Election Results")
print("__________ _________")

print(f"Total Votes: {row_count:,}")
print("___________ ___________")
for k in range (0,candicount):
    print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:})")
print("_______________ _____________")
print(f"Winner: {candilist[winner]}")


