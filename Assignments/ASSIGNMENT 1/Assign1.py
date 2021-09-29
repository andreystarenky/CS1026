# Andrey Starenky
# Assign 1
# CS1026A
# September 28, 2021

# Constant Prices
OFF_PEAK_PRICE = 0.085
ON_PEAK_PRICE = 0.176
MID_PEAK_PRICE = 0.119

# Constant Discounts
TOTAL_USAGE_DISCOUNT = 0.04
ON_PEAK_DISCOUNT = 0.05
SENIOR_DISCOUNT = 0.11

# Constant Tax
TAX = 0.13

while True: # loop forever until break; is called
    # get input for off peak time
    offPeakInput = float(input("Enter kwh during Off Peak period: "))

    if offPeakInput == 0: # if off peak input is 0 then break out of the loop
        break # break out of the loop

    # Get on peak input
    onPeakInput = float(input("Enter kwh during On Peak period: "))
    # Get mid peak input
    midPeakInput = float(input("Enter kwh during Mid Peak period: "))
    # Get is senior input
    isSeniorInput = input("Is owner senior? (Y,y,N,n): ")

    # Calculate Prices Prior to Discounts
    offPeakCost = offPeakInput * OFF_PEAK_PRICE
    onPeakCost = onPeakInput * ON_PEAK_PRICE
    midPeakCost = midPeakInput * MID_PEAK_PRICE

    # Calculate Discounts
    # Total Usage Discount


    # On Peak Discount
    if onPeakInput<150 and offPeakInput<400:
        onPeakCost *= (1-ON_PEAK_DISCOUNT)

    # Total Cost
    totalCost = offPeakCost + onPeakCost + midPeakCost

    if offPeakInput+onPeakInput+midPeakInput<400:
        totalCost *= (1-TOTAL_USAGE_DISCOUNT)

    # Senior Discount
    if isSeniorInput == 'Y' or isSeniorInput == 'y':
        totalCost *= (1-SENIOR_DISCOUNT)

    # TAX
    totalCost *= (1+TAX)

    # Output result
    print("Electricity cost: $" + "%.2f" % (totalCost))