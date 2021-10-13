
# ACTIVITY
def factorial(n):
    result = n
    for i in range(2,n):
        result *= i
    return result

print(factorial(5))

def countVowels(word):
    numVowels = 0            # First error numVowels should be 0
    for letter in word:      # Second error string instead of word
        if letter.lower() in "aeiou":  # Third error does not consider uppercase letters
            numVowels += 1
    return numVowels         # Fourth error returns letter (not defined) instead of the number of vowels

print(countVowels("AEIOu"))