# EC601-A2
EC601 A2 Haochuan Hu
huhc@bu.edu


1. sign up and get key in https://developer.twitter.com/en

2. download the sample codes
Twitter-API-v2-sample-code-main is some sample codes from twitter official:
https://github.com/twitterdev/Twitter-API-v2-sample-code

and I found a really useful library and its document: https://docs.tweepy.org/en/stable/examples.html
Then I use python to get access to twitter API
download library using 
```bash
pip install requests
pip install tweepy
```


Here are some testing codes.
```python
client = tweepy.Client(bearer_token)

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

response = client.search_recent_tweets("Tweepy")
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

# Each Tweet object has default ID and text fields
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)

# By default, this endpoint/method returns 10 results
# You can retrieve up to 100 Tweets by specifying max_results
response = client.search_recent_tweets("Tweepy", max_results=100)
```
