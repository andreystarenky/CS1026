# Andrey Starenky, astarenk, 251214306
# November 17, 2021
# This is the sentiment_analysis module
# It has one function which has a responsibility of computing and returning
# average happiness scores of each of the 4 regions based on a set of tweets

# This function will compute and return the avg happiness score, total number of keyword tweets, and
# total number of tweets by region given the name of a file containing tweets and a file containing keywords
def compute_tweets(nameOfTweetsFile, nameOfKeysFile):
    try: # try statement is used in case of the files not existing
        tweetsFile = open(nameOfTweetsFile, "r", encoding="utf-8")
        keysFile = open(nameOfKeysFile, "r", encoding="utf-8")

    except FileNotFoundError as e: # Except the error if file is not found
        print(e)
        return [] # Return blank array, files do not need to be closed since they were not found

    keys = {}  # create dictionary for keywords and their values

    for line in keysFile:  # get keys and their values
        keyword = line[:line.index(',')]  # take the word up to the first comma
        value = int(line[(line.index(',') + 1):].strip())  # take the word after the first comma until new line character
        keys[keyword] = value  # add key and its respective value to the dict

    # Define constants for checking coordinates
    TOP = 49.189787
    BOTTOM = 24.660845
    START_EDGE = -125.242264

    PACIFIC_EDGE = -115.236428
    MOUNTAIN_EDGE = -101.998892
    CENTRAL_EDGE = -87.518395
    EASTERN_EDGE = -67.444574

    # Order of the regions
    regionsListOrder = ['Eastern', 'Central', 'Mountain', 'Pacific']

    # create a nested dict to store the data for each region
    # each region dict will have its own dict with totalScore, numTweets, and numKeyTweets values
    # ** please note the totalScore is stored instead of avg so avg can be calculated after the loop

    regionsData = {}

    # give each region it's own dict holding the num of tweets and key tweets, and total for average in the end
    for region in regionsListOrder: # this is to save redundancy with copy paste
        regionsData[region] = {'numTweets': 0, 'numKeyTweets': 0, 'totalScore': 0, 'avg':0}

    # Loop through all lines in the file, all tweets
    for line in tweetsFile:
        lineList = line.split()

        # get the lat and long values
        lat = float(lineList[0].replace('[','').replace(',','')) # remove [ ] and , from the lat and long values
        long = float(lineList[1].replace(']', ''))

        # check that the tweet is within the main boundary
        if long > START_EDGE and long < EASTERN_EDGE and lat < TOP and lat > BOTTOM:
            # tweet is in boundaries --> get sentiment score
            # sublist for the tweet as it always starts with the 5th list item
            # this is done in the case that any keyword in the future might contain or be numbers
            tweetList = lineList[5:]

            # Get the sentiment value
            sentimentValue = getSentimentValue(tweetList, keys)

            # Check if the coords fall in which zones
            if long < PACIFIC_EDGE: # check pacific
                addToRegionDict(regionsData['Pacific'], sentimentValue)
            elif long < MOUNTAIN_EDGE: # check mountain
                addToRegionDict(regionsData['Mountain'], sentimentValue)
            elif long < CENTRAL_EDGE: # check central
                addToRegionDict(regionsData['Central'], sentimentValue)
            else: # must be eastern
                addToRegionDict(regionsData['Eastern'], sentimentValue)


    for region in regionsData: # calculate avg for each
        if regionsData[region]['numKeyTweets'] > 0: # Avoid division by 0 if no values
            regionsData[region]['avg'] = regionsData[region]['totalScore'] / regionsData[region]['numKeyTweets']

    resultsList = []

    # create a tuple for each region and add it to the list to return
    for regionName in regionsListOrder:
        # tuple is (avg, number of keyword tweets, number of tweets)
        myTuple = (regionsData[regionName]['avg'], regionsData[regionName]['numKeyTweets'], regionsData[regionName]['numTweets'])
        resultsList.append(myTuple)

    # Close files
    tweetsFile.close()  # These are placed here instead of in the try because the only exception to be caught is file not existing
    keysFile.close()  # thus closing them in the finally statement would not make sense as they wouldn't open if an exception is caught

    return resultsList

# This function gets the sentiment value of a tweet using a tweet (list of words) and a dict of keywords
def getSentimentValue(tweet, keys):
    # Default values
    sentiment = 0
    numKeyWords = 0  # used to divide later

    # loop thru the array
    for word in tweet:
        # remove punctuation from beginning and end of tweet
        word = word.strip('!\"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~')
        word = word.lower() # convert word to lowercase

        if word in keys: # check if it has the key
            sentiment += keys[word] # add the sentiment value of the keyword to the total
            numKeyWords += 1 # increase total number by 1

    # Check if no key words to avoid division by 0
    if numKeyWords>0:
        sentiment/=numKeyWords

    return sentiment # return sentiment

# This function updates a given region's dict with the total happiness score and adds 1 to number of tweets and key tweets
def addToRegionDict(regionDict, sentiment):
    regionDict['numTweets'] += 1 # Add to total num of tweets
    if sentiment > 0: # If it is a key tweet
        regionDict['numKeyTweets'] += 1 # Add one to number of key tweets
        regionDict['totalScore'] += sentiment # Add value to total score