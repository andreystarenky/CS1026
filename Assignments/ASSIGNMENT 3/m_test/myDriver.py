from sentiment_analysis import compute_tweets

results = compute_tweets("tweets.txt","keywords.txt")
regions = ['Eastern', 'Central', 'Mountain', 'Pacific']

for index in range(0,len(results)):
    print(regions[index] + ' - Happiness Score: ' + str(results[index][0]) + ' Keyword Tweets: ' + str(results[index][1]) + ' Total Tweets: ' + str(results[index][2]))
