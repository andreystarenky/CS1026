# Andrey Starenky, astarenk, 251214306
# December 4, 2021
# This module has the processUpdates function which will take care of checking the files and handling updates

from catalogue import CountryCatalogue

def processUpdates(cntryFileName, updateFileName, badUpdateFile):
    # Create catlog variable
    catlog = None

    # This is a looping variable - if file is found, it will be set to true otherwise it will loop until
    # a valid file name is given
    valid = False

    while not valid:
        # Check the countries file first
        try:
            countriesFile = open(cntryFileName, 'r', encoding="utf-8")
            countriesFile.close()  # Close file
            # File is valid
            # Create countries catalogue with the new data
            catlog = CountryCatalogue(cntryFileName)
            print("Countries file successfully processed . . .")
            valid = True # Reset loop variable to exit loop

        except FileNotFoundError:
            print("Countries file does not exist!")
            # Ask for quit
            if input("Would you like to quit? (Y/N) ").lower() == 'n': # If user enters N or n, continue
                # Not quitting, prompt for new file name
                cntryFileName = input("Enter the new countries file name: ")
            else:
                # Write to output file
                outputUnsuccessfulUpdate()
                return False, None

    # Do the same thing with updates file
    listOfUpdates = []
    valid = False # Loop variable
    while not valid:
        # Check the updates file
        try:
            updatesFile = open(updateFileName, 'r', encoding="utf-8")
            # Add the updates to the list of updates
            for line in updatesFile:
                listOfUpdates.append(line.strip().replace(' ','')) # Remove spaces, clean up string
            updatesFile.close()  # Close file
            print("Updates file successfully processed . . .")
            valid = True

        except FileNotFoundError:
            print("Updates file does not exist!")
            # Ask for quit
            if input("Would you like to quit? (Y/N) ").lower() == 'n':  # If user enters N or n, continue
                # Not quitting, prompt for new file name
                updateFileName = input("Enter the new updates file name: ")
            else:
                # Write to output file
                outputUnsuccessfulUpdate()
                return False, None
    #print(listOfUpdates)

    # handle all updates, and add to invalid updates list if the update is invalid
    invalidUpdates = []
    for update in listOfUpdates:
        if handleUpdate(update, catlog):
            print("Processed update: " + update)
        else:
            print("!!!!!!!!!!!!!!!!!!!Invalid update: " + update)
            invalidUpdates.append(update)


def handleUpdate(update, catlog):
    if update == "":  # Empty update
        print("empty update")
        return False
    updateArray = update.split(';')  # Remove spaces, and split using ; character
    if len(updateArray) == 1:  # Only country, no updates
        print("only country no udpate")
        return False
    countryName = updateArray[0]
    if countryName[0].islower():  # If first character is not uppercase
        print("first char is lower")
        return False
    for char in countryName:  # Check if each character in the word is allowed
        if (char.lower() < 'a' or char.lower() > 'z') and char != '_':
            print("country char out of bounds")
            return False
    return True
    #   COMMAS IN GROUPS OF 3

    return True

def validateNumber(value):
    return False

def outputUnsuccessfulUpdate():
    try:
        myFile = open("output.txt", 'w', encoding="utf-8")
        myFile.write("Update Unsuccessful\n")
        myFile.close()
    except Exception as e:
        print("Could not open file: " + str(e))