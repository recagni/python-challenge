#------------------------------------------------------------------------------------------------------------
#                               PYPARAGRAPH
#------------------------------------------------------------------------------------------------------------
#    1) FILE IMPORT AND INIIAL QUESTIONS TO USERS
#------------------------------------------------------------------------------------------------------------

# Import modules.  

# "re" is a processor used later for converting regular expressions into internal representations that are 
# used by the system.  In this case, for instance, to split words and paragraphs.

# "shutil" is a module used for operations on files and collection of files.  In this case, the "copy" command
# within shutil was used to create a copy of the original files.

# "fileinput" was imported to edit the original text file.
 
import os
import re
import shutil
import fileinput

# Monitor user interest in seeing another data set.

Monitor="y"
while Monitor=="y":

    # Ask user to point to the desired data set.  This question makes this code modular, in that it allows the 
    # user to use this code with any data set, as long as it is a .txt file.

    dataSet=input("Please type the paragraph number (1 or 2) for which you'd like to see the statistics:  ")

    # Define path to txt file.
    origPath = os.path.join("raw_data","paragraph_" + str(dataSet) + ".txt")

    # Open the text file, with the intent of reading it ("r").
    xxx = open(origPath,"r")

    # Read the text file, meaning that it converts the file from a TextIOWrapper into a normal string ready to
    # be read.
    origFile=xxx.read()

#------------------------------------------------------------------------------------------------------------
#    2) IMPORTED FILE MODIFICATION
#------------------------------------------------------------------------------------------------------------

    # The second proposed data set happens to have no spaces after the periods, which slightly alter the word
    # count and severely compromise the sentence count.  So, we need to modify the imported files so that we 
    # can be sure that all periods are followed by a space.  To do so, we first make a copy of the original 
    # file that we place in the same folder as the original one (but obviously with a different name).

    newPath= os.path.join("raw_data","new_paragraph_" + str(dataSet) + ".txt")
    shutil.copyfile(origPath,newPath)

    # In the new file, make the desired replacements, meaning that all the periods are substitutes by periods
    # followed by an empty space.
    newFile = origFile.replace(".", ". ")

#------------------------------------------------------------------------------------------------------------
#   3) WORD COUNT CALCULATION
#------------------------------------------------------------------------------------------------------------

    # Make use of the function "re.findall" which is part of the imported module "re".
    wordCount = len(re.findall("[a-zA-Z_]+", newFile))

#------------------------------------------------------------------------------------------------------------
#   4) SENTENCE COUNT CALCULATION
#------------------------------------------------------------------------------------------------------------

    # Make use of the function "re.split" which is part of the imported module "re".
    # The addition of "-1" at the end is to take into account of the fact that (see above section 2) the 
    # original file was modified via Python so that spaces are added after periods.
    # In addition, a dollar sign was added in the original formula, this too to improve the algorithm.
    # However, because the algorithm is ineherently imprecise (people write text as they please), the 
    # sentence count doesn't necessarily give the exact result.
    sentenceCount=len(re.split("(?<=[.!?$]) +", newFile))-1

#------------------------------------------------------------------------------------------------------------
#   5) AVERAGE LETTER COUNT CALCULATION
#------------------------------------------------------------------------------------------------------------

    # Make use of the function "re.findall" which is part of the imported module "re".
    letterCount = len(re.findall("[A-Za-z]", newFile))
    
    # Average letter count is given simply by total letters divided by total words.
    avgLetterCount=letterCount/wordCount

#------------------------------------------------------------------------------------------------------------
#   6) AVERAGE SENTENCE LENGTH CALCULATION
#------------------------------------------------------------------------------------------------------------

    # Average sentence lenght is given simply by total words divided by total sentences (paragraphs).
    avgSentenceCount=wordCount/sentenceCount

    # HOWEVER, DUE TO WHAT MENTIONED ABOVE (SEE SECTION 2) THE NUMBERS FOR THE SECOND DATA SET ARE OFF.

#------------------------------------------------------------------------------------------------------------
#   7) PRINTING OPERATIONS AND FINAL USER MONITORING
#------------------------------------------------------------------------------------------------------------

    print ("----------------------------------------")
    print ("Paragraph Analysis of Paragraph Number ",(dataSet))
    print ("----------------------------------------")
    print ("Approximate Word Count: "+ str(wordCount)) 
    print ("Approximate Sentence Count: " + str(sentenceCount))
    print ("Average Letter Count: " + str(avgLetterCount))
    print ("Average Sentence Length: " + str(avgSentenceCount))
    print ("----------------------------------------")

# Monitor user interest in continuining to see other data sets

    Monitor=input("Would you like to see the statistics for another paragraph? Please type yes (y) or no (n):   ")
    #------------------------------------------------------------------------------------------------------------