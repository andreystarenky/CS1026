# Andrey Starenky
# Lab 2
# CS1026A
# September 29, 2021

'''
clientAge = float(input("Please enter your age in years: "))
if(clientAge>=9):
    clientHeight = float(input("Please enter your height in cm: "))
    if(clientHeight>=130):
        print("You may go on the ride")
    else:
        print("Sorry you are too short to go on the ride")
else:
    print("Sorry, you are too young for this ride")
'''

IDEAL_CREDIT_SCORE = 720
userScore = int(input("Please enter your credit score: "))
housePrice = int(input("Please enter the price of the house: "))

if userScore >= IDEAL_CREDIT_SCORE: # switched => to >=
    downPayment = 0.1 * housePrice
elif userScore < IDEAL_CREDIT_SCORE and userScore > 600: # switched else if to elif, and "600" to 600
    downPayment = 0.2 * housePrice
else:
    downPayment = 0.3 * housePrice # was not indented

print("Your down payment is: ${}".format(downPayment))