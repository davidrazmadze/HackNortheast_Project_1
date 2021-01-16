import json

with open('tweets.json') as f:
    data = json.load(f)

    # Iterate over each key
    for item in data:
        print(item['text'])
