import os
import csv



count_votes = 0
candidate_list = {}
candidate_won = ""
candidate_vote_count = 0
candidate_percent_won = 0


csvpath = os.path.join("Resources", "election_data.csv")


with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")


    csv_header = next(csv_file)



    for row in csv_reader: 
       
     
        count_votes += 1 
        

        if(row[2] not in candidate_list):
            candidate_list[row[2]] = 1
        else:
            candidate_list[row[2]] += 1

    for candidate in candidate_list:
        if(candidate_vote_count < candidate_list[candidate]):
            candidate_vote_count = candidate_list[candidate]
            candidate_won = candidate



with open(os.path.join("analysis","output.txt"), 'w') as outfile:
    
    print("Election Results")
    outfile.write('Election Results\n')
    print(f"Total Votes: {count_votes}")
    outfile.write(f"Total Votes: {count_votes}"+'\n')
    for k,v in candidate_list.items():
        print(f"{k}:{round(v/count_votes * 100, 3)}% ({v})")
        outfile.write(f"{k}:{round(v/count_votes * 100, 3)}% ({v})"+'\n')
    print(f"Winner: {candidate_won}")
    outfile.write(f"Winner: {candidate_won}"+'\n')