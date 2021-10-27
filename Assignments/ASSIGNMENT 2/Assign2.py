# Andrey Starenky
# astarenk 251214306
# Assign 1
# CS1026A
# October 06, 2021
# This program checks codes inputted by the user to determine the algorithms used by checking potential options against the check code

# Import the code_check.py file
import code_check

# Initialize code lists
basicList = []
positionList = []
upcList = []
noneList = []

# Loop until broken out by input of 0
while True:
    # Get user input
    userInput = input("Please enter code (digits only) (enter 0 to quit) ")

    # Check if input is 0
    if userInput == "0":
        break

    # Make a default none variable - when the code gets added to a list, this will become false
    none = True

    # Check for basic code
    if code_check.checkBasic(userInput):
        basicList.append(userInput) # Add to list
        print("-- code: " + userInput + " valid Basic code.")
        none = False # None is false, as one code matched

    # Check for position code
    if code_check.checkPosition(userInput):
        positionList.append(userInput) # Add to list
        print("-- code: " + userInput + " valid Position code.")
        none = False # None is false, as one code matched

    # Check for UPC code
    if code_check.checkUPC(userInput):
        upcList.append(userInput) # Add to list
        print("-- code: " + userInput + " valid UPC code.")
        none = False # None is false, as one code matched

    # If none is still true, none of the codes matched
    if none:
        noneList.append(userInput) # Add to none list
        print("-- code: " + userInput + " not Basic, Position or UPC code.")

#Summary
print("Summary")
# Basic Codes
print("Basic: ", end = "")
# Print out each code
for x in range(0,len(basicList)):
    # IF LAST ITEM, DON'T PRINT COMMA
    if (x == len(basicList) - 1):
        print(basicList[x], end="")
    else: # ELSE PRINT COMMA
        print(basicList[x], end=", ")
# If no codes, print none
if(len(basicList) == 0):
    print("None")
else:
    print()

# Position Codes
print("Position: ", end = "")
# Print out each code
for x in range(0,len(positionList)):
    # IF LAST ITEM, DON'T PRINT COMMA
    if (x == len(positionList) - 1):
        print(positionList[x], end="")
    else: # ELSE PRINT COMMA
        print(positionList[x], end=", ")
# If no codes, print none
if(len(positionList) == 0):
    print("None")
else: print()

# UPC Codes
print("UPC: ", end = "")
for x in range(0,len(upcList)):
    # IF LAST ITEM, DON'T PRINT COMMA
    if (x == len(upcList)-1):
        print(upcList[x], end="")
    else: # ELSE PRINT COMMA
        print(upcList[x], end=", ")
# If no codes, print none
if(len(upcList) == 0):
    print("None")
else:
    print()

# None Codes
print("None: ", end = "")
for x in range(0,len(noneList)):
    # IF LAST ITEM, DON'T PRINT COMMA
    if (x == len(noneList) - 1):
        print(noneList[x], end="")
    else:  # ELSE PRINT COMMA
        print(noneList[x], end=", ")
# If no codes, print none
if(len(noneList) == 0):
    print("None")
else: print()