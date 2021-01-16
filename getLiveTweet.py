import tweepy
import time
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


global x


class MyStream(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        print(status.user.id_str)
        print(status.user.followers_count)
        print(status.favorite_count)
        print(status.retweet_count)
        global mystream_Text, mystream_Favorite_Count, mystream_retweet_count, mystream_user_id_str, mystream_Follower_Count
        #x = tweety(status.text, status.favorite_count, status.retweet_count, status.user.id_str, status.user.followers_count)
        x = status.text
        return False


mstream = MyStream()
myStreamListen = tweepy.Stream(auth=api.auth, listener=mstream)
myStreamListen.filter(follow=["1292952619611295763"])
print(x)
