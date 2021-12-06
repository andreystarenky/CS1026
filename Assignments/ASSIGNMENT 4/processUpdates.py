# Andrey Starenky, astarenk, 251214306
# December 4, 2021
# This module has the processUpdates function which will take care of checking the files and handling updates

from catalogue import CountryCatalogue
from country import Country

def processUpdates(cntryFileName, updateFileName, badUpdateFile):
    # Create catlog variable
    catlog = None
    
!!!! Why catlog and not catalog?    

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
                
!!! It's a really bad prctice to use a paramenter as a variable (assigning to it)
!!! Normally you'd create a new variable first thing inside this function like fileName = cntryFileName, and then use this one
!!! Same for the updateFile

    USE ONE VAR NAME
                
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
                
!!! DO YOU HAVE TO CHECK IF THE LINE IS EMPTY AND SKIP IT?                
                
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
            
!!!! do you need to remove this !!!!!!! print thing?            
            
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


def handleUpdate(update, catlog):
    if update == "":  # Empty update
        print("empty update")
        
!!! Instructions say that "If there is a blank line in the file, it should be skipped. " - so completely blank update is not invalid
!!! maybe you can just skip even creating an update for it when reading a file if the line is blank
        
        return False
    if update.count(';') > 3:  # Too many semicolons
        return False
    updateArray = update.split(';')  # Remove spaces, and split using ; character
    
!!! Suggestion: extract these into separate function like parseName(updateArray) that returns (True, Name) or (False, None)
    
    countryName = updateArray[0]
    if len(countryName) == 0:  # Country field is empty
        print("country is empty")
        return False
    if countryName[0].islower():  # If first character is not uppercase
        print("first char is lower")
        return False
    for char in countryName:  # Check if each character in the word is allowed
        if (char.lower() < 'a' or char.lower() > 'z') and char != '_':
            print("country char out of bounds")
            return False

!!! This doesn't look like it will work for the countries with the spaces in them like United_ States _ of_America
!!! this is valid (after the spaces are removed), but won't pass your validation.
        
    # At this point, the country name is valid - we can now proceed to check for what updates to make

    if len(updateArray) == 1:  # Only country name, with no updates
        # ADD COUNTRY WITH NO DATA - the addCountry function already checks if it exists so no need to do that here
        catlog.addCountry(countryName)
        return True  # No need to continue here, if only the country name is given this is the only update to make

    # Counters for each type of update
    numP, numA, numC = 0, 0, 0
    # ! ! ! Important ! ! !
    # We must loop through the array once ONLY to check for problems and NOT to make any updates
    # This is because if there is a single error, the entire update should be ignored
    # This is to prevent finding an error on the last field once all the other updates have been applied
    for item in updateArray:
        if item != countryName:  # Make sure we are not dealing with the country name, the first index
            
!!! You should be doing index loop from 1.
!!! What if I have an update record: France;France;France ? - all elements are the same and you'd happily skip them
            
            if len(item) > 2:  # Make sure the update is not blank or just 2 chars (also invalid)
                # We are assuming that for every X= there will be a value following it, otherwise it is ignored
                if item[1] == '=':  # Make sure there is an equals sign
                    valueString = item[2:]  # This is the string with the actual value to update with
                    if item[0] == 'P' and numP == 0:  # Check if it is P and if there have been no P updates yet
                        numP +=1
                        if not validateNumber(valueString):  # Check if the population is value (commas)
                            print("invalid pop")
                            return False
                    elif item[0] == 'A' and numA == 0:
                        numA +=1
                        if not validateNumber(valueString):  # Check if the area is value (commas)
                            print("invalid area")
                            return False
                    elif item[0] == 'C' and numC==0:
                        numC +=1
                        if not validateContinent(valueString):
                            print("invalid continent")
                            return False
                    else:               # Not a valid update field character, or an update field has been given more than once
                        print("invalid field char or given more than once")
                        return False
                else:
                    return False  # No equals sign
            elif len(item) > 0:
                print("1 char or no val")
                return False  # Invalid field (only 1 character OR no field value (such as "P=")
            # Else ignore, no need to handle empty field

    # If this point is reached, the update should be determined to be VALID
    # Time to process the update!
    # No more need to catch invalid update, just check if there is an update field

    searchCountry = Country(countryName)

    # CHECK IF NEED TO ADD COUNTRY
    if catlog.findCountry(searchCountry) == None:
        # Country does not exist, first add it to the catlog
        catlog.addCountry(countryName)  # We only need to add the name, the rest of the values will be added below

    for item in updateArray:
        
!!! YOU don't need a second loop. You can just start building these updates in the first one:
!!! pUpdate= ""
!!! aUpdate = ""
!!! cUpdate = ""
!!! AND INSTEAD of the counters you just check if these are empty inside the loop, like instead of checking numP == 0 you check len(pUpdate) == 0
!!! and then instead of numP += 1 you do if validateNumber() : pUpdate = <value>
!!! much simpler and elegant
        
        if item != countryName:  # Make sure we are not dealing with the country name, the first index
            if len(item) > 2:  # Make sure the update is not blank - if it is, it is skipped
                    valueString = item[2:]  # This is the string with the actual value to update with
                    if item[0] == 'P':  # Process P update
                        catlog.findCountry(searchCountry).setPopulation(valueString)

                    elif item[0] == 'A':
                        catlog.findCountry(searchCountry).setArea(valueString)

                    elif item[0] == 'C':
                        catlog.findCountry(searchCountry).setContinent(valueString)

                    # Should not be any other case, but end with elif just in case to catch potential bad updates

    return True

# Validate population and area values
def validateNumber(value):
    reversedValue = value[::-1]  # Reverse the string
    for i in range(0, len(reversedValue)):  # Iterate through string backwards
        if (i + 1) % 4 == 0:  # Check if in position where comma should be
            if reversedValue[i] != ',':  # Check for comma where it should be
                return False
            
!!! CHECK THAT THE NUMBER DOESN'T START WITH A COMMA            
            
        elif reversedValue[i] == ',':  # Check for comma where it should not be
            
!!! THIS SHOULD CHECK FOR A VALID DIGIT INSTEAD            
            
                return False

        #elif not value[i].isdigit():  # Return false if a character is not a digit
            #return False
    return True

# Validate continent values
def validateContinent(value):
    continents = ['Africa', 'Antarctica', 'Arctic', 'Asia', 'Europe', 'North_America', 'South_America']
    if value not in continents:
        return False
    else:
        return True

def outputUnsuccessfulUpdate():
    try:
        myFile = open("output.txt", 'w', encoding="utf-8")
        myFile.write("Update Unsuccessful\n")
        myFile.close()
    except Exception as e:
        print("Could not open file: " + str(e))
