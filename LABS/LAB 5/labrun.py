# Activity 1

myList = []
while True:
    userInput = input("Enter an integer: ")
    if myList.count(int(userInput)) == 0:
        myList.append(int(userInput))
    if len(myList) == 10:
        break

print("Contents of list: " + str(myList))


#Activity 2

myList2 = ["bob", 'e', '12321', 'max', 'p1234321p'] # Output should be 3 (bob, 12321, p1234321p
count = 0
for x in myList2:
    if len(x)>1 and x[0] == x[-1]:
        count += 1
print(count)


# PART 2
# Section 1

def zFirst(words):
     # We will need two lists
     zresult =[]
     result =[]
     for word in words:
         if word.lower()[0] == 'z':
             # If it does, add it to the first list
             zresult.append(word)
         else:
             # Does not begin with a 'z'
             result.append(word)

     zresult.sort()
     result.sort()
     return zresult + result

words=["hello","good","nice","as","at","baseball","absorb","sword","a","tall","so",
       "bored","silver","hi","pool","we","am","seven","do","you","want","ants","because","that's",
       "how","you","get","zebra","zealot","zoo","xylophone","asparagus"]
print(zFirst(words))

# Section 2
values = [1,2,3,4,5]
newValues = values.copy() # must copy array instead of passing reference
for i in range(len(values)): # remove +1
  newValues[i] +=1 # values changed to newValues
  print("Old Value at index {} is: {} ".format(i, values[i])) # newValues changed to values
  print("New Value at index {} is: {} \n".format(i, newValues[i]))