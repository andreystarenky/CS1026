evenSet = set()
oddSet = set()
threeSet = set()

for i in range(0,21):
    if i % 2 == 0:
        evenSet.add(i)
    if i>0 and i%2==1:
        oddSet.add(i)
    if i>0 and i%3==0:
        threeSet.add(i)

myDict = {}

myDict['even'] = evenSet
myDict['odd'] = oddSet
myDict['three'] = threeSet

for entry in myDict:
    print(entry + ": " + str(myDict[entry]))

'''
f = open("rawdata.txt","r")  
incomeDict = {}  
countryDict = {}  
countryList = []  
incomeList = []  
initialList = []  
  
for line in f:  
    line = line.upper().strip("\n").split(":")  
    initialList.append(line[1][0])  
    countryList.append(line[1])  
    incomeList.append(line[2])  
  
for i in range(0, len(countryList)):  
  incomeDict[countryList[i]] = incomeList[i]  
  if initialList[i] in countryDict:  
    countryDict[initialList[i]].add(countryList[i])  
  else:  
    countryDict[initialList[i]] = {countryList[i]}  
  
done = False  
while not done:  
  text = input("Enter an initial or a country name: ")  
  text = text.upper()  
  if text == "QUIT":  
    done = True  
  elif text in countryDict:  
    print(countryDict[text])  
  elif text in incomeDict:  
    print(incomeDict[text])  
  else:  
    print("Does not exist.")
'''

