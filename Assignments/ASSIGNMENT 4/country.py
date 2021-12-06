# Andrey Starenky, astarenk, 251214306
# December 4, 2021
# This file contains the Country class, which contains information about a single country
# This includes its name, population, area, and continent

class Country:
    # Constructor with default values
    def __init__(self, name, pop="", area="", continent=""):
        # Define the variables in an instance context
        self.name = name
        self.population = pop
        self.area = area
        self.continent = continent


    # Getter methods
    def getName(self):
        return self.countryName

    def getPopulation(self):
        return self.population

    def getArea(self):
        return self.area

    def getContinent(self):
        return self.continent

    # Setter methods
    def setPopulation(self, newPop):
        self.countryPopulation = newPop

    def setArea(self, newArea):
        self.countryArea = newArea

    def setContinent(self, newCont):
        self.countryContinent = newCont

    # String representation method
    def __repr__(self):
        return self.countryName + " (pop: " + self.population + ", size: " + self.area + ") in " + self.continent

