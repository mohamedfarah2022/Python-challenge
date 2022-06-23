#import os and csv
import csv
import os

#create path file towards csv file
csvpath = os.path.join("..", "Resources", "election_data.csv")
csvpath_output = ("..", "analysis","election_data.txt")

#determine variables to be used
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

#use DictReader
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)

#to allow the votes to be tallied.
    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        



        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    # Determine the Winner:
    if (votes > winner_votes):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row["Candidate"]
    
    
    #printed lines for the thhe script to run
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")

#results printed posistion showing the votes and the percentage in a string
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 

candidate_votes

 #Winner to be decided
winner = sorted(candidate_votes.items(),)

#results
print("-------------------------")
print("Winner: " + str(winner[1]))
print("-------------------------")

output_file = os.path.join("pyPoll.txt")

# Output Files
with open(output_file, "w") as datafile:
    
    print("Election Results", file=datafile)
    print("-------------------------", file=datafile)
    print("Total Votes " + str(votes),file=datafile)
    print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")",file=datafile)
    print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    print(str(winner),file=datafile)
    print("-------------------------",file=datafile)
    print("Winner: " + str(winner[1]),file=datafile)
    print("-------------------------",file=datafile)