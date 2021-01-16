import tweepy
import time
import os
from keys import consumer_key
from keys import consumer_secret
from keys import key
from keys import secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

class tweety(tweepy.StreamListener):
    def __init__(self, text1, likes1, retweets1, user1, follower1):
        text = text1                # text of tweet
        likes = likes1              # number of likes tweet has
        retweets = retweets1        # number of retweets it has
        user = user1                # username of tweeter
        follower = follower1        # follower count of user who posted tweet

ticker = input("Enter Stock Ticker: ")
numTweet = 6
global tick
with open('HackNortheast_Project_1\\t2n.txt') as file:
    for line in file:
        if ticker in line:
            print(f'{ticker} FOUND')
            tick = line

print("===================")
for tweet in tweepy.Cursor(api.search, q=tick, lang='en').items(numTweet):
    try:
        print(f"Tweet received; Text: \n{tweet.text} ---- {tweet.user.screen_name}")
        if ticker in tweet.text:
            print(f"{ticker} FOUND")
    except tweepy.error.TweepError as er:
        print(er.reason)
    except StopIteration:
        break