# Andrey Starenky, astarenk, 251214306
# December 6, 2021
# This module has the processUpdates function which will take care of checking the files and handling updates
# It will also use various helper functions

from catalogue import CountryCatalogue
from country import Country

# Global Constant so it does not need to be recreated each time the validateContinent() function is called
CONTINENTS = ['Africa', 'Antarctica', 'Arctic', 'Asia', 'Europe', 'North_America', 'South_America']

# Main function to process updates
def processUpdates(cntryFileName, updateFileName, badUpdateFile):
    # Create catlog variable
    catlog = None

    # This is a looping variable - if file is found, it will be set to true otherwise it will loop until
    # a valid file name is given
    valid = False

    tempFileName = cntryFileName

    while not valid:
        # Check the countries file first
        try:
            countriesFile = open(tempFileName, 'r', encoding="utf-8")
            countriesFile.close()  # Close file
            # File is valid
            # Create countries catalogue with the new data
            catlog = CountryCatalogue(tempFileName)
            print("Countries file successfully processed . . .")
            valid = True # Reset loop variable to exit loop

        except FileNotFoundError:
            print("Countries file does not exist!")
            # Ask for quit
            if input("Would you like to quit? (Y/N) ").lower() == 'n': # If user enters N or n, continue
                # Not quitting, prompt for new file name
                tempFileName = input("Enter the new countries file name: ")
            else:
                # Write to output file
                outputUnsuccessfulUpdate()
                return False, None

    # Set temp file name variable to the updates one
    tempFileName = updateFileName

    # Do the same thing with updates file
    listOfUpdates = []
    valid = False # Loop variable
    while not valid:
        # Check the updates file
        try:
            updatesFile = open(tempFileName, 'r', encoding="utf-8")
            # Add the updates to the list of updates
            for line in updatesFile:
                if line.strip() != "":  # Check that line is not empty
                    listOfUpdates.append(line.strip().replace(' ','')) # Remove spaces, clean up string
                
            updatesFile.close()  # Close file
            print("Updates file successfully processed . . .")
            valid = True

        except FileNotFoundError:
            print("Updates file does not exist!")
            # Ask for quit
            if input("Would you like to quit? (Y/N) ").lower() == 'n':  # If user enters N or n, continue
                # Not quitting, prompt for new file name
                tempFileName = input("Enter the new updates file name: ")
            else:
                # Write to output file
                outputUnsuccessfulUpdate()
                return False, None

    # handle all updates, and add to invalid updates list if the update is invalid
    invalidUpdates = []
    for update in listOfUpdates:
        if not handleUpdate(update, catlog):
            invalidUpdates.append(update)

    # Add bad updates to file
    try:
        writeFile = open(badUpdateFile, 'w',  encoding="utf-8")
        for item in invalidUpdates:
            writeFile.write(item + "\n")
        writeFile.close()
    except Exception as e:
        print("Error opening file for writing: " + str(e))

    # Print the new updated list of countries to "output.txt"
    catlog.saveCountryCatalogue("output.txt")

    return True, catlog


# Handle each individual update
def handleUpdate(update, catlog):
    if update.count(';') > 3:  # Too many semicolons
        return False
    updateArray = update.split(';')  # Remove spaces, and split using ; character

    countryName = updateArray[0]
    if not validateCountry(countryName):
        return False

    # At this point, the country name is valid - we can now proceed to check if the updates are valid

    if len(updateArray) == 1:  # Only country name, with no updates
        # ADD COUNTRY WITH NO DATA - the addCountry function already checks if it exists so no need to do that here
        catlog.addCountry(countryName)
        return True  # No need to continue here, if only the country name is given this is the only update to make

    # Update strings for each type of update
    pUpdate, aUpdate, cUpdate = "", "", ""
    # ! ! ! Important ! ! !
    # We must loop through the array once to check for problems and collect any updates but only apply them after the loop
    # This is because if there is a single error, the entire update should be ignored
    # This is to prevent finding an error on the last field once all the other updates have been applied
    for item in updateArray[1:]:  # Test the sub-array not including the country
        if len(item) > 2:  # Make sure the update is not blank or just 2 chars (also invalid)
            # We are assuming that for every X= there will be a value following it, otherwise it is ignored
            if item[1] == '=':  # Make sure there is an equals sign
                valueString = item[2:]  # This is the string with the actual value to update with
                if item[0] == 'P' and pUpdate == "":  # Check if it is P and if there have been no P updates yet
                    if not validateNumber(valueString):  # Check if the population is value (commas)
                        return False
                    pUpdate = valueString
                elif item[0] == 'A' and aUpdate == "":  # Check if it is A and if there have been no A updates yet
                    if not validateNumber(valueString):  # Check if the area is value (commas)
                        return False
                    aUpdate = valueString
                elif item[0] == 'C' and cUpdate == "":  # Check if it is C and if there have been no C updates yet
                    if not validateContinent(valueString):
                        return False
                    cUpdate = valueString
                else:  # Not a valid update field character, or an update field has been given more than once
                    return False
            else:
                return False  # No equals sign
        elif len(item) > 0:
            return False  # Invalid field (only 1 character OR no field value (such as "P=")
        # Else ignore, no need to handle empty field

    # If this point is reached, the update should be determined to be VALID
    # Time to process the update!
    # No more need to catch invalid update, just perform the updates

    searchCountry = Country(countryName)

    # CHECK IF NEED TO ADD COUNTRY
    if catlog.findCountry(searchCountry) == None:
        # Country does not exist, first add it to the catlog
        catlog.addCountry(countryName)  # We only need to add the name, the rest of the values will be added below

    # Create the updates
    # Population update
    if pUpdate != "":  # If not empty
        catlog.findCountry(searchCountry).setPopulation(pUpdate)

    # Area update
    if aUpdate != "":  # If not empty
        catlog.findCountry(searchCountry).setArea(aUpdate)

    # Continent update
    if cUpdate != "":  # If not empty
        catlog.findCountry(searchCountry).setContinent(cUpdate)

    return True


# Validate the country name
def validateCountry(countryName):
    if len(countryName) == 0:  # Country field is empty
        return False
    if countryName[0].islower():  # If first character is not uppercase
        return False
    for char in countryName:  # Check if each character in the word is allowed
        if (char.lower() < 'a' or char.lower() > 'z') and char != '_':
            return False
    return True


# Validate population and area values
def validateNumber(value):
    if value[0] == ",":  # Checks if first character is a ',' such as ,300 which is invalid
        return False
    reversedValue = value[::-1]  # Reverse the string
    for i in range(0, len(reversedValue)):  # Iterate through string backwards
        if (i + 1) % 4 == 0:  # Check if in position where comma should be
            if reversedValue[i] != ',':  # Check for comma where it should be
                return False
        elif not reversedValue[i].isdigit():  # Check for non digit where it should not be (comma can be in other spot but not here)
            return False
    return True


# Validate continent values
def validateContinent(value):
    return value in CONTINENTS


# Outputs unsuccessful to file
def outputUnsuccessfulUpdate():
    try:
        myFile = open("output.txt", 'w', encoding="utf-8")
        myFile.write("Update Unsuccessful\n")
        myFile.close()
    except Exception as e:
        print("Could not open file: " + str(e))
