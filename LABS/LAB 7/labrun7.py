'''
# Activity
values = [1,2,3,4,5,"hello",6,7,8,9,"10"]

for cur in values:
    print("The value is :", values[cur])
    if type(values[cur]) == str:
        raise ValueError("This is a string!")
'''

filename = input("Enter filename: ")
try:
    infile = open(filename, "r")
    line = infile.readline()
    value = int(line)

except FileNotFoundError:
    print("No such file")

except ValueError:
    print("Value is not an int")
