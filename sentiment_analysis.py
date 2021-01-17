import json
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    return score


# 1. Open text file
text = open('sentiment_example.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# 2. Token the words
tokenized_words = word_tokenize(cleaned_text, "english")

# 3. Removing Stop Words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# 4. Lemmatization - From plural to single + Base form of a word (example better-> good)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)

# 5. Print out if you percentage to buy the stock
with open('tweets.json') as f:
    data = json.load(f)
    max_possible_score = 0
    actual_score = 0.0

    i = 0
    j = 0
    k = 0
    print("i: " + str(i) + " j: " + str(j) + " k: " + str(k))

    # Iterate over each object in json file
    for item in data:
        text = item['text']
        followers_count = item['followers_count']
        likes = item['likes']
        retweet_count = item['retweet_count']
        compound = sentiment_analyse(text)['compound']

        temp_sum = (followers_count+i) + (likes+j) + (retweet_count+k)
        max_possible_score += temp_sum
        actual_score += temp_sum * compound

    # Calculate percentage
    actual_score += max_possible_score
    max_possible_score *= 2
    finalPercentage = (actual_score / max_possible_score) * 100
    finalPercentage = str(round(finalPercentage, 2))
    print("There is a " + str(finalPercentage) +
          "% change this stock will be a good buy")
