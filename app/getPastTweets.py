import tweepy
import time
import datetime
import os
import json
import sys
from keys import consumer_key
from keys import consumer_secret
from keys import key
from keys import secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def get_relevant_tweets(ticker, number_of_tweets, days_ago):
    tweet_list = []  # list to hold tweets fetched
    global tick
    with open('/Users/raz/Desktop/HackNortheast_Project_1/app/t2n.txt') as file:
        for line in file:
            if ticker in line:
                tick = line
                yesterday = datetime.datetime.now() - datetime.timedelta(days=days_ago)
                tick = tick.strip('\n') + f' -filter:retweets' + \
                    f' since:{yesterday.strftime("%Y-%m-%d")}'
                print(tick)
    for tweet in tweepy.Cursor(api.search, q=tick, lang='en').items(number_of_tweets):
        try:
            print(
                f"Tweet received; Text: \n{tweet.text} ---- {tweet.user.screen_name} ---- {tweet.created_at}")
            tweet_list.append(tweet)
        except tweepy.error.TweepError as er:
            print(er.reason)
        except StopIteration:
            break
    return tweet_list


def store_tweets_in_json(passed_tweet_list, file):
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
    file_to_open = open(file, 'w')
    json.dump(tweet_list, file_to_open, indent=4, sort_keys=True)
    file_to_open.flush()
    file_to_open.close()


def get_past_tweets(control_ticker, tweets_to_open, days_past):
    alltweets = get_relevant_tweets(control_ticker, tweets_to_open, days_past)
    store_tweets_in_json(
        alltweets, '/Users/raz/Desktop/HackNortheast_Project_1/app/relevant_tweets.json')
