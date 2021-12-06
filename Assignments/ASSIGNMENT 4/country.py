# Andrey Starenky, astarenk, 251214306
# December 4, 2021
# This file contains the Country class, which contains information about a single country
# This includes its name, population, area, and continent

class Country:
    # Constructor with default values
    def __init__(self, name, pop="", area="", continent=""):
        # Define the variables in an instance context
        self.countryName = name

!!! THESE HAVE TO BE NAMED WITHOUT "country" - just name, population, area, continent. 
you can do this.name = name, the first one is the instance variable, the second is a paramenter     

        self.countryPopulation = pop
        self.countryArea = area
        self.countryContinent = continent


    # Getter methods
    def getName(self):
        return self.countryName

    def getPopulation(self):
        return self.countryPopulation

    def getArea(self):
        return self.countryArea

    def getContinent(self):
        return self.countryContinent

    # Setter methods
    def setPopulation(self, newPop):
        self.countryPopulation = newPop

    def setArea(self, newArea):
        self.countryArea = newArea

    def setContinent(self, newCont):
        self.countryContinent = newCont

    # String representation method
    def __repr__(self):
        return self.countryName + " (pop: " + self.countryPopulation + ", size: " + self.countryArea + ") in " + self.countryContinent

    # Override the equals operator for checking if this object is equal to another
    def __eq__(self, other):
        if other!= None and self.countryName == other.getName():
            return True
        
!!! WE DISCUSSED THIS - you don't need this. And it is also wrong, as 2 country objects with the same name 
and different other fields would be considered equal

        return False
