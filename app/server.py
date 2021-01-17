from getLiveTweet import get_live_tweets
from getPastTweets import get_past_tweets
from sentiment_analysis import performAnalysis
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/square/', methods=['POST'])
def square():
    stockName = request.form['text']
    isLive = request.form['isLive']

    # Fetch tweets
    if isLive == "true":
        print("Now viewing live tweets:")
        get_live_tweets(stockName)

        # TODO: Perform sentiment analysis
        data = {'percentage': 0.05}
        data = jsonify(data)
        return data
    else:
        print("Past tweets")
        tweets_to_open = request.form['numTweetsInput']
        days_past = request.form['numDaysInput']
        get_past_tweets(stockName, int(tweets_to_open), int(days_past))

        # Perform sentiment analysis
        percentage = performAnalysis('relevant_tweets.json')

        # Return percentage
        data = {'percentage': percentage}
        data = jsonify(data)
        return data


if __name__ == '__main__':
    app.run(debug=True)
