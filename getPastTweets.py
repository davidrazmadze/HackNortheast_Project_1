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

def get_relevant_tweets(ticker, number_of_tweets):
    tweet_list = [] # list to hold tweets fetched
    global tick
    with open('HackNortheast_Project_1\\t2n.txt') as file:
        for line in file:
            if ticker in line:
                tick = line
    for tweet in tweepy.Cursor(api.search, q=tick, lang='en').items(number_of_tweets):
        try:
            print(f"Tweet received; Text: \n{tweet.text} ---- {tweet.user.screen_name}")
            tweet_list.append(tweet)
            if ticker in tweet.text:
                print(f"{ticker} FOUND")
                
        except tweepy.error.TweepError as er:
            print(er.reason)
        except StopIteration:
            break
    return tweet_list
def store_tweets_in_json(tweet_list, file='relevant_tweets.json'):
    


if __name__ == '__main__':
    ticker = input("Enter stock ticker OR company name: ")
    tweets_to_open = int(input("How many tweets would you like to retrieve?"))
    print(get_relevant_tweets(ticker, tweets_to_open))
