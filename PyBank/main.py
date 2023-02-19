# import os module
import os # allow for operating system/file handling functions

# import module for csv files
import csv

# use os.path.join to form a path to the csv file
csvFilePath = os.path.join("Resources", "budget_data.csv")



# use the with open() function to open the csvFilePath into an object
with open(csvFilePath) as csvFile:
# csv module .reader() function specifies the delimiter and object name for the reader in the open() function
    csvReader = csv.reader(csvFile, delimiter = ",")

    # the csvReader has the info in the file, split into rows of lists
    # that correspond to each row of data in the file

    # if the first row has header data, use next() to pass over the row
    header = next(csvReader) # skips the first row
    print("Financial Analysis")
    print("\n----------------------------\n")
    
    # all my variables that I need that will be callable outside of a for loop.
    # I'm pretty sure I could have done it an easier way by this was the best I could do.
    total_months = 0
    sum = 0
    sum2 = 0
    NextRow = []
    PrevRow = []
    DiffRow = []
    Allmonths = []
    max = 0
    min = 99999999999999999999999

    for row in csvReader:
        # setting the first column to a variable
        months = row[0]
        # setting the second column to a variable but also making sure that it converts everything from a string to an integer
        profit_loss = int(row[1])
        # This goes through the list an adds each item once in the list of months (list of strings) and stores it in an variable that was established earlier
        total_months += months.count(row[0])
        # this adds up all of the integers column 2 
        sum += profit_loss
        
        # to my understanding, this is the only way to make the list callable outside of the for loop
        # This allow me manipulate it once the for loop has run
        # I created NextRow and PrevRow so that I could find the difference in profits. First I needed to use excel to get a 
        # clearer understand of what I needed to do and how to make two lists of the same length and properly subtract them,
        # then DiffRow was created
        NextRow.append(int(row[1]))
        PrevRow.append(int(row[1]))
        Allmonths.append(row[0])
    
    # remove the first item in list
    NextRow.pop(0)
    # remove the last item in list
    PrevRow.pop()
    # now the two lists are of the same length but most importantly, they are properly aligned in order to subract the two lists
    # to calculate the difference in profit from month to month
    # in order to perform operations between two lists, I needed to zip them
    DiffRow = [NextRow - PrevRow for NextRow, PrevRow in zip(NextRow, PrevRow)]

    for r in DiffRow:
        sum2 += int(r) # add up the differences from the list. I need this to calculate the Average change in profit/loss
    
    for maximum in DiffRow:
        if maximum > max:
            max = maximum # captures the maximum change in DiffRow list

    for minimum in DiffRow:
        if minimum < min:
            min = minimum # captures the minimum change in DiffRow list

    indexmax = (DiffRow.index(max)) # stored the index number of the maximum difference to a variable
    indexmin = (DiffRow.index(min)) # stored the index number of the minimum difference to a variable

    # These are all my prints
    print(f"Total Months: {total_months}\n")
    print(f"Total: ${sum}\n")
    print(f"Average Change: ${round((sum2/(total_months - 1)),2)}\n") # (total month - 1) is necessary because there maybe,
    # for example 50 months but there will only be 49 differencs between those months
    print(f"Greatest Increase in Profits: {Allmonths[indexmax+1]} (${max})\n") # (indexmax +1) or (indexmin +1) is necessary because
    # in order to do the calculation I needed to pop out a value from NextRow[] and in order to get the corresponding month
    # in Allmonths[], I needed to add one
    print(f"Greatest Decrease in Profits: {Allmonths[indexmin+1]} (${min})")

# this creates the new text file
textFile = open("analysis/PyBank_Results.txt", "w")

# this prints info to the text file
textFile.write("Financial Analysis")
textFile.write("\n----------------------------\n")
textFile.write(f"Total Months: {total_months}\n")
textFile.write(f"Total: ${sum}\n")
textFile.write(f"Average Change: ${round((sum2/(total_months - 1)),2)}\n")
textFile.write(f"Greatest Increase in Profits: {Allmonths[indexmax+1]} (${max})\n")
textFile.write(f"Greatest Decrease in Profits: {Allmonths[indexmin+1]} (${min})")

# this closes the open text file
textFile.close()
