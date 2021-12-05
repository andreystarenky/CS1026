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
            countriesFile = open(cntryFileName, 'r')
            countriesFile.close()

            catlog = CountryCatalogue(cntryFileName)
            valid = True

        except FileNotFoundError:
            print("File does not exist!")
            # Ask for quit
            if input("Would you like to quit? (Y/N) ").lower() == 'n':
                # Not quitting, prompt for new file name
                cntryFileName = input("Enter the new countries file name: ")
            else:
                return False, None

    # do updates crap here