# Andrey Starenky, astarenk, 251214306
# November 17, 2021
# This is the main python file that will request an input for the file names and get the values from compute_tweets
# from the sentiment_analysis module

from sentiment_analysis import compute_tweets # Import function

# Call compute_tweets with the inputs of the user
results = compute_tweets(input("please enter the name of the tweets file: "), input("please enter the name of the keywords file: "))
regions = ['Eastern', 'Central', 'Mountain', 'Pacific'] # Order of the regions for output
for index in range(0,len(results)): # For each region results, print the output score, and totals
    print(regions[index] + ': Happiness Score: ' + str(results[index][0]) + ', ' + str(results[index][1]) + ' keyword tweets, ' + str(results[index][2]) + " tweets in total for the region")
