# Hack the Northeast - Sentiment Analysis of Tweets based on Stock

## How to run

* Note: make sure you have all requirements installed. see 'requirements.txt'

```
cd app
python3 server.py
```

Open up a browser, and go to 'http://127.0.0.1:5000/' or what ever it says in the terminal window

## Description of project

Performs sentiment analysis on a tweets involving stocks to inform user whether to buy, hold, or sell a particular stock.

## [nltk - Natural Language Toolkit](http://www.nltk.org)

### List of nltk packages

- twitter_samples

- punkt

- wordnet

- averaged_perceptron_tagger

- pos_tag

- stop_words

### How to install nltk datasets/packages

```
raz@Davids-MacBook-Pro ~ % python3
>>> import nltk
>>> nltk.download_shell()
NLTK Downloader
---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d

Download which package (l=list; x=cancel)?
  Identifier> twitter_samples
```
