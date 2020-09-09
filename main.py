import tweepy
import random
import time
import sys

auth = tweepy.OAuthHandler("",
        "")

auth.set_access_token("",
        "")

api = tweepy.API(auth)

# 30 or so of these tweets will take place before the turn of the hour
n_tweets = 30 + 100

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
                random.choice(verb_options) + ", " + \
                " which make robots like me!\n" + \
                "#PurdueRobotClub #PurdueDayOfGiving (" + \
                str(n) + "/" + str(n_tweets) + ")"
        
        if len(tweet) < 250:
           break 

    # print(tweet)
    return tweet

def get_wait_time():
    t = time.localtime()
    return (((5+16) - t.tm_hour) * 36000 +
            (59 - t.tm_min) * 60 +
            52 - t.tm_sec)

def spam(n_tweets=10):
    for i in range(n_tweets):
        tweet = construct_tweet(i+1)
        api.update_status(tweet)


while True:
    if  get_wait_time() > 30:
        print("sleeping for " + str(get_wait_time()) + " seconds")
        time.sleep(get_wait_time()-30)
    elif get_wait_time() > 0:
        time.sleep(1)
        print("sleeping for 1 second")
    else:
        print("time to make some money")
        start_time = time.time()
        spam(n_tweets)
        duration = time.time() - start_time
        break

time.sleep(1)
api.update_status("PDOG interaction bot has finished at " + time.strftime("%H:%M:%S") + \
    "\nif you enjoyed make sure you donate! @PurdueRobotClub #PurdueDayOfGiving")
print("sent " + str(n_tweets) + " tweets in " + str(duration) + " seconds")
