# Andrey Starenky, astarenk, 251214306
# December 4, 2021
# This file contains the CountryCatalogue class which holds the info for all the countries
# It can also find and add countries and save the catalogue of the countries

from country import Country

class CountryCatalogue:
    # Constructor with default values
    def __init__(self, countryFileName):
        # Create a dictionary to store the Country objects - dict easier to find by names later
        self.myCountries = {}

!!! IT HAS TO BE NAMED countryCat

        # Get data from file
        countryFile = open(countryFileName, 'r', encoding="utf-8")
        countryFile.readline() # skip the first line as it is just a header
        for line in countryFile:
            # Clean up string from mainly '\n' characters, and split it by the '|' character
            lineArray = line.strip().split('|')

!!! So we are not doing any validation here that the line is not emppty, that we read exactly 4 values
!!! It doesn't say that we should be doing validations, but I'm just checking (I think it's OK)
                                                                               
            # Create a country object to add to list of countries
            newCountry = Country(lineArray[0],lineArray[2],lineArray[3],lineArray[1])
            self.myCountries[lineArray[0]] = newCountry


    # Setter methods
    def setPopulationOfCountry(self, countryName, newValue):
        # Check if country exists - should not get to this point if DNE because it should check prior to this
                                                                               
!!! COPY THIS COMMENT TO THE OTHER SETTERS?                                    
                                                                               
        if countryName in self.myCountries:
            self.myCountries[countryName].setPopulation(newValue)
        else:
            print("Error - country DNE: " + countryName)

    def setAreaOfCountry(self, countryName, newValue):
        if countryName in self.myCountries:
            self.myCountries[countryName].setArea(newValue)
        else:
            print("Error - country DNE: " + countryName)

    def setContinentOfCountry(self, countryName, newValue):
        if countryName in self.myCountries:
            self.myCountries[countryName].setContinent(newValue)
        else:
            print("Error - country DNE: " + countryName)

    # Find country method
    def findCountry(self, countryObject):
        if countryObject.getName() in self.myCountries:
            return self.myCountries[countryObject.getName()]
        return None

    # Add country method
    def addCountry(self, countryName, pop="", area="", cont=""):  # Parameters with default values of ""
        tempCountry = Country(countryName, pop, area, cont)
        # Check if country already exists
        if self.findCountry(tempCountry) == None:

!!! YOU ARE NOT USING findCountry in setters, but you use directly "if countryName in self.myCountries" so why use it here?
!!! DO THE SAME: if not countryName in self.myCountries:
!!!                 self.myCountries[countryName] = Country(countryName, pop, area, cont)
!!! DO not need tempCountry at all
                                                                               
            # Country is not in our Catalogue yet
            self.myCountries[countryName] = tempCountry
            return True
        return False

    # Method to print the Country Catalogue
    def printCountryCatalogue(self):
        for country in self.myCountries:
            print(self.myCountries[country])

    # Method to save the Catalogue to a file
    def saveCountryCatalogue(self, fname):
        # Keep track of number of items to return at end of function
        numItems = -1

        # Make a list (to sort the countries later) and add all the countries (formatted) to it
        outputList = []
        for country in self.myCountries:
            # Format for output
            currentCountry = self.myCountries[country]
            tempString = currentCountry.getName() + '|' + currentCountry.getContinent() + '|' + currentCountry.getPopulation() + '|' + currentCountry.getArea()
            outputList.append(tempString)
            numItems += 1

        # Sort the list
        outputList.sort()

        try:
            outputFile = open(fname, 'w', encoding="utf-8")
            outputFile.write("Country|Continent|Population|Area\n") # Write a header to the output file
            for line in outputList:
                outputFile.write(line + '\n')
            outputFile.close()
        except Exception as e:
            print("Error opening file for writing: " + str(e))
            numItems = -1
        finally:
            return numItems
