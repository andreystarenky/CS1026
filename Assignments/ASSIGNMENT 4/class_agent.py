from country import Country
from catalogue import CountryCatalogue
from processUpdates import *

'''
c1 = Country("Canada", "38,123,531", "31,820,793", "North America")

print(c1)
c1.setContinent("Asia")
c1.setArea("2 lmao")
c1.setPopulation("at least 4")
print(c1.getName())
print(c1.getPopulation())
print(c1.getArea())
print(c1.getContinent())
print(c1)
'''

'''
myCat = CountryCatalogue('data.txt')

testCountry = Country("Italy", "59,801,004", "300,000", "Europe")
testCountry2 = Country("fake_country", "123", "456", "Asia")

myCat.printCountryCatalogue()

print()

print(myCat.findCountry(testCountry)) # yes
print(testCountry)

print()

# GOOD
#print(myCat.addCountry("Italy", "59,801,004", "300,000", "Europe"))
print(myCat.addCountry("Fake_country", "123", "456", "Asia"))

# GOOD
#myCat.setAreaOfCountry("United_States_of_America", "44")
#myCat.setContinentOfCountry("Canada", "Asia")
#myCat.setPopulationOfCountry("China", "7")

print()
print("############### FINAL OUTPUT ###############")
#myCat.printCountryCatalogue()
myCat.saveCountryCatalogue("output.txt")



#myCat = CountryCatalogue('data.txt')
#print(myCat.saveCountryCatalogue("output.txt"))
'''



BAD_UPDATE_FILE = "badupdates.txt"
cntryFileName = input("Enter name of file with country data: ")
updateFileName = input("Enter name of file with country updates: ")
result, catlog = processUpdates(cntryFileName,updateFileName,BAD_UPDATE_FILE)
print()
print(40*"*")
if result:
    print("*** Updating successfully completed")
    catlog.printCountryCatalogue()
else:
    print("*** Updating NOT successfully completed")
