# Andrey Starenky, astarenk, 251214306
# December 6, 2021
# This file contains the Country class, which contains information about a single country
# This includes its name, population, area, and continent

# Country Class
class Country:
    # Constructor with default values
    def __init__(self, name, pop="", area="", continent=""):
        # Define the variables in an instance context
        self.name = name
        self.population = pop
        self.area = area
        self.continent = continent


    # Getter methods
    # Return name
    def getName(self):
        return self.name

    # Return population
    def getPopulation(self):
        return self.population

    # Return area
    def getArea(self):
        return self.area

    # Return continent
    def getContinent(self):
        return self.continent

    # Setter methods
    # Set population
    def setPopulation(self, newPop):
        self.population = newPop

    # Set area
    def setArea(self, newArea):
        self.area = newArea

    # Set continent
    def setContinent(self, newCont):
        self.continent = newCont

    # String representation method
    def __repr__(self):
        return self.name + " (pop: " + self.population + ", size: " + self.area + ") in " + self.continent

