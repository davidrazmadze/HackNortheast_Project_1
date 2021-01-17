from getLiveTweet import get_live_tweets
from getPastTweets import get_past_tweets

if __name__ == '__main__':
    control_ticker = input("Enter Ticker Symbol for Company: ")
    selection = input("Type \'Live\' to see Live Tweets or type \'Past\' to see past tweets:")
    while selection == 'Live' or selection == 'Past':
        if selection == 'Live':
            print("Now viewing live tweets:")
            get_live_tweets(control_ticker)
            break
        if selection == 'Past':
            get_past_tweets(control_ticker)
            print("\n All tweets are stored in a json for easy access.")
            break
