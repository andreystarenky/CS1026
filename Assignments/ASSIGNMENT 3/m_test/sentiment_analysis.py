def compute_tweets(tweets, keywords):
    try:  # assuming both text files exist
        # define constants
        charsToStrip = ".,!@#$%^&*()?<>[]{}|/_+=:;\"\\"
        numbOfRegions = 4
        regionCountOfTweets = [0]*numbOfRegions  # E, C, M, P
        regionCountOfKWTweets = [0]*numbOfRegions  # E, C, M, P
        regionTotalHappy = [0]*numbOfRegions  # E, C, M, P
        regionAverageHappy = [0]*numbOfRegions  # E, C, M, P
        retList = [""]*numbOfRegions
        # opening text files
        tweetsFile = open(tweets, "r", encoding="utf-8")  # opening tweets
        keywordsFile = open(keywords, "r", encoding="utf-8")  # opening keywords
        # iterate over every tweet, word, and keyword to find matches
        for currentTweet in tweetsFile:  # for each tweet
            happyTotal = 0  # reset happiness score
            countKeywords = 0  # reset count of keywords
            region = determineRegion(currentTweet.split())  # determine tweet region
            if region != "":  # if tweet is outside relevant regions
                for word in currentTweet.split():  # for each word in the tweet
                    for keyword in keywordsFile:  # for each keyword line
                        if keyword.split(",")[0] == word.strip(charsToStrip).lower():
                            happyTotal += int(keyword.split(",")[1])
                            countKeywords += 1
                    keywordsFile.seek(0)  # sends cursor back to top of keywordsFile so it can be iterated over again
                # after processing each tweet, update regional counts for tweets, KWtweets, and averagehappy
                regionCountOfTweets[region] += 1
                if region == 1:
                   print(currentTweet)
                if happyTotal > 0:
                    happyTotal = happyTotal/countKeywords
                    regionCountOfKWTweets[region] += 1
                    regionTotalHappy[region] += happyTotal
                    regionAverageHappy[region] = regionTotalHappy[region]/regionCountOfKWTweets[region]
        # after processing all tweets, take totals from region lists, and place into tuples in list, to be returned
        for i in range(numbOfRegions):
            retList[i] = (regionAverageHappy[i], regionCountOfKWTweets[i], regionCountOfTweets[i])
    except FileNotFoundError:  # in the case that the text files don't exist, return a blank list
        retList = []
    return retList


def determineRegion(tweet):
    yCoord = float(tweet[0].strip("[],"))
    xCoord = float(tweet[1].strip("[],"))
    yTopBound = 49.189787
    yBotBound = 24.660845
    xRightBound = -67.444574
    xEasternBound = -87.518395
    xCentralBound = -101.998892
    xMountainBound = -115.236428
    xPacificBound = -125.242264
    if yBotBound <= yCoord <= yTopBound and (xRightBound >= xCoord):
        if xCoord >= xEasternBound :  # its in eastern
            return 0
        elif xCoord >= xCentralBound:  # its in central
            return 1
        elif xCoord >= xMountainBound:  # its in mountain
            return 2
        elif xCoord >= xPacificBound:  # its in pacific
            return 3
    return ""
