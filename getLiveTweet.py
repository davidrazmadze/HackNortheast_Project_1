import tweepy
import time
import sys
import json
import os
from keys import consumer_key
from keys import consumer_secret
from keys import key
from keys import secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

global x
class MyStream(tweepy.StreamListener):
    def on_status(self, status):
        tweet_live = []
        tweet_live.append(status)
        store_last_tweet_in_json(tweet_live)
        print(status.text)
        print(status.user.id_str)
        print(status.user.followers_count)
        print(status.favorite_count)
        print(status.retweet_count)

    def on_error(self, error):
        print(error)

def store_last_tweet_in_json(passed_tweet_list):
    tweet_list = []
    for tweet in passed_tweet_list:
        tweet_info = dict()
        tweet_info['text'] = tweet.text
        tweet_info['creation'] = tweet.created_at.strftime("%m-%d-%Y %H:%M:%S")
        tweet_info['screen_name'] = tweet.user.screen_name
        tweet_info['retweet_count'] = tweet.retweet_count
        tweet_info['likes'] = tweet.favorite_count
        tweet_info['followers_count'] = tweet.user.followers_count
        tweet_list.append(tweet_info)
    file_to_open = open('HackNortheast_Project_1\\last_live_tweet.json', 'w')
    json.dump(tweet_list, file_to_open, indent = 4, sort_keys=True)
    file_to_open.flush()
    file_to_open.close()

if __name__ == '__main__':
    mstream = MyStream()
    myStreamListen = tweepy.Stream(auth = api.auth, listener = mstream)
    myStreamListen.filter(follow=["1292952619611295763"])
