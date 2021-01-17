from getLiveTweet import get_live_tweets
from getPastTweets import get_past_tweets
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/square/', methods=['POST'])
def square():
    stockName = request.form['text']
    isLive = request.form['isLive']

    if isLive == "true":
        print("Now viewing live tweets:")
        get_live_tweets(stockName)
    else:
        print("Past tweets")
        tweets_to_open = request.form['numTweetsInput']
        days_past = request.form['numDaysInput']
        get_past_tweets(stockName, int(tweets_to_open), int(days_past))
        print("\nAll tweets are stored in a json for easy access.")

    # square = num ** 2
    # data = {'square': square}
    # data = jsonify(data)
    return "Ok"


if __name__ == '__main__':
    app.run(debug=True)
