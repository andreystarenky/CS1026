# Check for basic code
def checkBasic(checkString):
    sum = 0 # Default sum is 0
    for x in checkString[0:-1]: # Loop through string EXCEPT last character
        sum += int(x) # Add digit to sum
    checkDigit = sum % 10 # Get mod 10
    if checkDigit == int(checkString[len(checkString) - 1]):
        return True # Return True if the check digit matches the given input
    return False

# Check for position code
def checkPosition(checkString):
    sum = 0 # Default sum is 0
    for x in range(0,len(checkString)-1):  # Loop through string EXCEPT last character
        sum += (int(checkString[x]) * (x + 1)) # Add the digit * position to the sum
    checkDigit = sum % 10 # Get mod 10
    if checkDigit == int(checkString[len(checkString) - 1]):
        return True # Return True if the check digit matches the given input
    return False

# Check for UPC code
def checkUPC(checkString):
    sum = 0 # Default sum is 0
    for x in range(0, len(checkString) - 1):  # Loop through string EXCEPT last character
        if (x + 1) % 2 == 1: # Check if odd position
            sum += (int(checkString[x]) * 3) # Add digit multiplied by 3 to sum
        else: # Else even position
            sum += int(checkString[x]) # Add digit to sum
    if (sum % 10 != 0):
        checkDigit = 10 - (sum % 10) # Get 10 - mod 10 if mod 10 is not 0
    else:
        checkDigit = 0

    if checkDigit == int(checkString[len(checkString) - 1]):
        return True # Return True if the check digit matches the given input
    return False