class Fruit():
    def canBePhone(self):
        return "fruits can't be phones"

class Banana(Fruit):
    def canBePhone(self):
        return "bananas can be phones!"

apple=Fruit()
print(apple.canBePhone())

banana=Banana()
print(banana.canBePhone())