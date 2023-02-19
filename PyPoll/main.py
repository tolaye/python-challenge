# import os module
import os # allow for operating system/file handling functions

# import module for csv files
import csv

# use os.path.join to form a path to the csv file
csvFilePath = os.path.join("Resources", "election_data.csv")



# use the with open() function to open the csvFilePath into an object
with open(csvFilePath) as csvFile:
# csv module .reader() function specifies the delimiter and object name for the reader in the open() function
    csvReader = csv.reader(csvFile, delimiter = ",")

    # the csvReader has the info in the file, split into rows of lists
    # that correspond to each row of data in the file

    # if the first row has header data, use next() to pass over the row
    header = next(csvReader) # skips the first row
    print("Election Results")
    print("\n-------------------------\n")

    # all my variables that I need that will be callable outside of a for loop.
    total_ballots = 0
    Candidate = []
    perStockham = 0.0
    perDeGette = 0.0
    perDoane = 0.0

    for row in csvReader:
        # setting the first column to a variable
        ballot = row[0]
        # This goes through the list an adds each item once in the list of ballots (list of strings) and stores it in
        # an variable that was established earlier
        total_ballots += ballot.count(row[0])

        # to my understanding, this is the only way to make the list callable outside of the for loop
        # This allow me manipulate it once the for loop has run
        # I created this list because I wanted to count from the list the amount of times a candidate won a vote
        Candidate.append(row[2])
    
    ball_Stockham = Candidate.count("Charles Casper Stockham") # stores the amounts of votes for Stockham
    ball_DeGette = Candidate.count("Diana DeGette") # stores the amounts of votes for DeGette
    ball_Doane = Candidate.count("Raymon Anthony Doane") # stores the amounts of votes for Doane

    # calculates the percentage votes won for each candidate
    perStockham = round(((ball_Stockham/total_ballots)*100),3)
    perDeGette = round(((ball_DeGette/total_ballots)*100),3)
    perDoane = round(((ball_Doane/total_ballots)*100),3)

    # These are all my prints
    print(f"Total Votes: {total_ballots}\n")
    print("-------------------------\n")
    print(f"Charles Casper Stockham: {perStockham}% ({ball_Stockham})\n")
    print(f"Diana DeGette: {perDeGette}% ({ball_DeGette})\n")
    print(f"Raymon Anthony Doane: {perDoane}% ({ball_Doane})\n")
    print("-------------------------\n")

    # this is for the last print statement. This determines, based on the count of votes who is the winner.
    # this compares the highest ballot count and prints the winner
    if ball_Stockham > ball_DeGette and ball_Stockham > ball_Doane:
        print("Winner: Charles Casper Stockham")
    elif ball_DeGette > ball_Stockham and ball_DeGette > ball_Doane:
        print("Winner: Diana DeGette")
    else:
        print("Winner: Raymon Anthony Doane")
    
    print("\n-------------------------\n")

# this creates the new text file
textFile = open("analysis/PyPoll_Results.txt", "w")

# this prints info to the text file
textFile.write("Election Results")
textFile.write("\n-------------------------\n")
textFile.write(f"Total Votes: {total_ballots}\n")
textFile.write("-------------------------\n")
textFile.write(f"Charles Casper Stockham: {perStockham}% ({ball_Stockham})\n")
textFile.write(f"Diana DeGette: {perDeGette}% ({ball_DeGette})\n")
textFile.write(f"Raymon Anthony Doane: {perDoane}% ({ball_Doane})\n")
textFile.write("-------------------------\n")


if ball_Stockham > ball_DeGette and ball_Stockham > ball_Doane:
    textFile.write("Winner: Charles Casper Stockham")
elif ball_DeGette > ball_Stockham and ball_DeGette > ball_Doane:
    textFile.write("Winner: Diana DeGette")
else:
    textFile.write("Winner: Raymon Anthony Doane")

textFile.write("\n-------------------------\n")

# this closes the open text file
textFile.close()
