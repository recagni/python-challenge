#------------------------------------------------------------------------------------------------------------
#                           PYBANK
#------------------------------------------------------------------------------------------------------------
#    1) FILE IMPORT AND INIIAL QUESTIONS TO USERS
#------------------------------------------------------------------------------------------------------------

# Import modules.  

# "operator" is used later for its function itemgetter.
# "sys" is used to create a .txt output.

import os
import csv
import operator
import sys

# Monitor user interest in seeing the results from another data set.

Monitor="y"
while Monitor=="y":

    # Ask user to point to the desired data set.  This question allows users to use this code with any data 
    # set, as long as the file Excel format is the same (more on this later in the "Note" below).

    dataSet=input("Please type the data set number (1 or 2) for which you'd like to see the statistics:  ")

    # Define path to CSV file.

    dataPath = os.path.join("raw_data","budget_data_" + str(dataSet) + ".csv")

#------------------------------------------------------------------------------------------------------------
#    2) VARIABLE DEFINITION
#------------------------------------------------------------------------------------------------------------

    # Create lists, initially empty, to store data.

    date = []
    revenue = []
    month = []
    year = []

#------------------------------------------------------------------------------------------------------------
#    3) FILE OPENING
#------------------------------------------------------------------------------------------------------------

    # Open the CSV file.

    # Note
    # The first column of the first data set seemed to have been formatted incorrectly in Excel, in that it 
    # was not formatted like the first column of the second data set, meaning MM-YY (rather than MM-DD).  
    # The expectation is that the data coming from the various sources be at least in the correct format.
    # Therefore, applying this code to the first set may give odd results, this not being due to the code. but
    # rather to the data set format.

    # If you were to print the CSV reader below (by coding "print yyy" right below it) you would obtain this 
    # cryptic result: <_yyy object at 0x000000...etc.>, typical of an object that will be manipulated.

    with open(dataPath, newline="") as xxx:
        yyy = csv.reader(xxx, delimiter=",")

        # Skip the headers.
        next(yyy,None)

        # Store the contents of the date and revenue columns into Python lists, by adding elements to them.
        for row in yyy:

            # Date: Add the elements in "row[0]" (i.e., first column of the CSV file) to the date list.
            # If you were to print the variable date below (with the instruction print(date) right below it),
            # you would find a relatively insignificant list of successive brackets like the following ones, 
            # as the code loops across the various columns of the first row of the CSV file.
            # ['Oct-12']
            # ['Oct-12', 'Nov-12']
            # etc.

            date.append(row[0])
            
            # Revenue: Add the integer of the elements in "row[1]" (i.e. second column of the CSV file) to 
            # the revenue list.

            revenue.append(int(row[1]))
            
            # Month: Add the left part (before the "-" delimiter, meaning the element 0 in the xxx list) of 
            # the elements in "row[0]" (first column of the CSV file) to the month list.

            zzz=row[0].split("-")
            month.append(zzz[0])
            
            # Year: Add the integer version of the right part (after the "-" delimiter, meaning the element 
            # 1 in the xxx list) of the elements in "row[1]" to the year list.

            year.append(int(zzz[1]))

#------------------------------------------------------------------------------------------------------------
#   4) MONTH RANGE CALCULATION
#------------------------------------------------------------------------------------------------------------
        
        # Convert the "month" list in the "integerMonth" list, expressed in integers, rather than dates.

        integerMonth=[]

        for i in month:
            if i=="Jan":
                i=1
                integerMonth.append(i)
            elif i=="Feb":
                i=2
                integerMonth.append(i)
            elif i=="Mar":
                i=3
                integerMonth.append(i)            
            elif i=="Apr":
                i=4
                integerMonth.append(i)            
            elif i=="May":
                i=5
                integerMonth.append(i)            
            elif i=="Jun":
                i=6
                integerMonth.append(i)            
            elif i=="Jul":
                i=7
                integerMonth.append(i)            
            elif i=="Aug":
                i=8
                integerMonth.append(i)            
            elif i=="Sep":
                i=9
                integerMonth.append(i)            
            elif i=="Oct":
                i=10
                integerMonth.append(i)            
            elif i=="Nov":
                i=11
                integerMonth.append(i)            
            else:
                i=12
                integerMonth.append(i)

        # Define the list "monthCount", which, for each of its elements, counts the total number of months 
        # starting from the year 2000.

        monthCount=[12*x + y for x, y in zip(year, integerMonth)]

        # The difference between the largest and smallest element in monthCount, plus one, is the total number
        # of months considered in the data set.
        # Note that, because of the above-mentined note in section 3, if we apply this code to the first
        # data set, we won't find correct values.

        monthRange=1+max(monthCount)-min(monthCount)

#------------------------------------------------------------------------------------------------------------
#   5) TOTAL REVENUE CALCULATION
#------------------------------------------------------------------------------------------------------------
        
        # Sum all the elements of the list revenue, previously defined as the integer part of the revenue 
        # column of the CSV file.

        totalRevenue=sum(revenue)

#------------------------------------------------------------------------------------------------------------
#   6) AVERAGE REVENUE CHANGE BETWEEN MONTHS CALCULATION
#------------------------------------------------------------------------------------------------------------
        
        # Sort the "revenue" list by date (oldest to newest), by first creating a tuple ("tupleMYR") from the 
        # lists "integerMonth" (i.s., the months expressed in numbers), "year'" and "revenue".
        # If you, below the next line, writes this:

        # for i in tupleMYR:
        #     print (i)

        # and run the code on the second data set, the output is a long list of unsorted sets of values like 
        # these (month, year, revenue):

        #     (1, 9, 943690)
        #     (2, 9, 1062565)
        #     etc.

        tupleMYR=zip(integerMonth,year,revenue)

        # Sort the tuple by date using the itemgetter operator.  The operator module was imported before.  
        # Itemgetter below is sorting first by year (position 1 in the just created tuple) and then by month 
        # (position 0).  If you, below the next line, write this:

        # print(sortedTriplets) 

        # and run the code, the output is the following list of triplets, sorted by year and then by month (2nd 
        # and 1st elements in each triplet):
        #    [(1, 9, 943690), (2, 9, 1062565), etc.]

        sortedTriplets = sorted(tupleMYR, key=operator.itemgetter(1,0))
      
        # Dylan's 11/19/17 note reads: "You can assume that each month shows up only once (one month per row), 
        # and that there are no duplicate months between the two files. Soon, we’ll deal with parsing dates in 
        # Python, but for now no need to worry about that."
        # This note basically allows us to ignore that the first data set to analyze has multiple values in 
        # each month, whilst the second one has only one value for each month.  Due to this, this code should 
        # really be tested on the second, not the first, data set.  If tested on the first one, it'll read the
        # years and months differently.

        # Extracts from the list of tuples, the first (month), second (year), and third (revenue) element, to 
        # create three separate lists to utilize later.
        
        sortedMonth=[]
        sortedYear=[]
        sortedRevenue=[]
        
        for i in sortedTriplets:
            sortedMonth.append(i[0])
            sortedYear.append(i[1])
            sortedRevenue.append(i[2])
        
        # Now the goal is to find the difference between consecutive elements of the list of sorted revenue.  
        # To do so, we first need to create a new list containinig all these differences.

        revenueDiff = [sortedRevenue[i+1]-sortedRevenue[i] for i in range(len(sortedRevenue)-1)]

        # Averages these differences to obtain the average revenue change between consecutive months.
        # Note that, because of the above-mentined note in section 3, if we apply this code to the first
        # data set, we won't find correct values.

        avgRevChange=sum(revenueDiff)/float(len(revenueDiff))
#------------------------------------------------------------------------------------------------------------
#   6) GREATEST MONTHLY REVENUE INCREASE CALCULATION
#------------------------------------------------------------------------------------------------------------
        # Maximum monthly revenue increase.
        maxRevInc=max(revenueDiff)  
    
        # Index on the revenueDiff list that matches the maximum monthly revenue increase.
        maxRevDiffIndex=revenueDiff.index(maxRevInc)

        # Month related to the maximum revenue increase, expressed in numbers.
        maxRevIncMonth=sortedMonth[maxRevDiffIndex]-1

        # Conversion in month name.

        Months=['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        maxRevIncMonthText=Months[maxRevIncMonth]

        # Largest monthly revenue increase.
        # Note that, because of the above-mentined note in section 3, if we apply this code to the first
        # data set, we won't find correct values.
        maxRevIncDate=(maxRevIncMonthText + "-" + str(sortedYear[maxRevDiffIndex]))

#------------------------------------------------------------------------------------------------------------
#   7) GREATEST MONTHLY REVENUE DECREASE CALCULATION
#------------------------------------------------------------------------------------------------------------

        # Mainimum monthly revenue increase.
        maxRevDec=min(revenueDiff)  
    
        # Index on the revenueDiff list that matches the minimum monthly revenue increase.
        minRevDiffIndex=revenueDiff.index(maxRevDec)-1

        # Month related to the minimum revenue increase, expressed in numbers.
        maxRevDecMonth=sortedMonth[minRevDiffIndex]

        # Conversion in month name.
        maxRevDecMonthText=Months[maxRevDecMonth]

        # Largest monthly revenue decrease.
        # Note that, because of the above-mentined note in section 3, if we apply this code to the first
        # data set, we won't find correct values.
        maxRevDecDate=(maxRevDecMonthText + "-" + str(sortedYear[minRevDiffIndex]))

#------------------------------------------------------------------------------------------------------------
#   8) PRINTING OPERATIONS AND FINAL USER MONITORING
#------------------------------------------------------------------------------------------------------------
        
        print ("-----------------------------------------")
        print ("Financial Analysis of Data Set Number ",(dataSet))
        print ("-----------------------------------------")
        print ("Total Months: " + str(monthRange))
        print ("Total Revenue: $" + str(totalRevenue))
        print ("Average Revenue Change: $" + str(avgRevChange))
        print ("Greatest Increase in Revenue: " + str(maxRevIncDate) + "  ($" + str(maxRevInc) + ")")
        print ("Greatest Decrease in Revenue: " + str(maxRevDecDate) + "  ($" + str(maxRevDec) + ")")
        print ("-----------------------------------------")

        # Monitor user interest in continuining to see other data sets
        Monitor=input("Would you like to see the statistics for another data set? Please type yes (y) or no (n):   ")   

#------------------------------------------------------------------------------------------------------------
#   9) TEXT FILE EXTRACTION
#------------------------------------------------------------------------------------------------------------

# Direct the standard output (stdout) to a text file located in the same folder as the code, by using the 
# "sys" module imported before.

sys.stdout = open('PyBank_Results.txt','wt')

print ("-----------------------------------------")
print ("Financial Analysis of Data Set Number ",(dataSet))
print ("-----------------------------------------")
print ("Total Months: " + str(monthRange))
print ("Total Revenue: $" + str(totalRevenue))
print ("Average Revenue Change: $" + str(avgRevChange))
print ("Greatest Increase in Revenue: " + str(maxRevIncDate) + "  ($" + str(maxRevInc) + ")")
print ("Greatest Decrease in Revenue: " + str(maxRevDecDate) + "  ($" + str(maxRevDec) + ")")
print ("-----------------------------------------")

#------------------------------------------------------------------------------------------------------------