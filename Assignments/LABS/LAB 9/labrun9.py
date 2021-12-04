class Car:
    def __init__(self):
        self._type = "none"

    def setType(self,type):
        self._type = type

    def getType(self):
        return self._type

# Create three cars
c1 = Car()
c2 = Car()
c3 = Car()

# Set their types
c1.setType("Toyota")
c2.setType("Honda")
c3.setType("Nissan")

# Print the types
print(c1.getType())
print(c2.getType())
print(c3.getType())