import tweepy
import random
import time
import sys

auth = tweepy.OAuthHandler("82s3u4xSfcrvRMXHnHI1HfJwI",
        "mxpjNhBjOi1KnfQMAn15QGDwdGgbcsU6ptUWsrkQSSNCPh0Zi6")

auth.set_access_token("1246318841963204608-vio3R1OMUccO1P90yoWqgK38u7ScnR",
        "q6GOuIkN9RTDwYv3GfxRzdBUbuYDtLZt9waOWiAfdpqPG")

api = tweepy.API(auth)

try:
    api.verify_credentials()
except:
    print("Error during auth")
    sys.exit()

with open('adjectives.txt', mode='r') as adj:
    adj_options = adj.read().split('\n')
    adj_options.pop()
    adj.close()

with open('noun.txt', mode='r') as noun:
    noun_options = noun.read().split('\n')
    noun_options.pop()
    noun.close()

with open('verb.txt', mode='r') as verb:
    verb_options = verb.read().split('\n')
    verb_options.pop()
    verb.close()

def construct_tweet(n):
    tweet =  ""
    while True:
        tweet = "It's " + \
                random.choice(adj_options) + " " + \
                random.choice(noun_options) + " " + \
                random.choice(verb_options) + " " + \
                "#PurdueRobotClub #purduedayofgiving (" + str(n) + "/50)"
        
        if len(tweet) < 250:
           break 

    print(tweet)
    return tweet
    

n_tweets = 0
while True:
    n_tweets += 1
    tweet = construct_tweet(n_tweets)
    api.update_status(tweet)
    if (n_tweets == 50):
        break
    time.sleep(1)

api.update_status("PDOG interaction bot has finished, if you enjoyed make sure you donate! @PurdueRobotClub #purduedayofgiving#")
