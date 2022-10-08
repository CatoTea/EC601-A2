# EC601-A2
EC601 A2 Haochuan Hu
huhc@bu.edu

## Start
1. sign up and get key in https://developer.twitter.com/en

2. download the sample codes
Twitter-API-v2-sample-code-main is some sample codes from twitter official:
https://github.com/twitterdev/Twitter-API-v2-sample-code

3. download library using 
```bash
pip install requests
pip install tweepy
```
I found a really useful library and its document: https://docs.tweepy.org/en/stable/examples.html
Then I use python to get access to twitter API


## Test
Here are some testing codes and result. (codes in TestAPI.py)

1. Search recent tweets:
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
Result:
```
{'newest_id': '1578570426283958272', 'oldest_id': '1578567909726642177', 'result_count': 10, 'next_token': 'b26v89c19zqg8o3fpzbn1e1xmre4etcqy15g75yoo3bzx'}
1578570426283958272
2022-10-08 02:18:12.640106 tweepy
1578570218691244032
@fuckyourputs IIRC, that was the value for the formal API route. Then I looked at a few of the python libraries (Twint, python-twitter, Tweepy, snsscrape or something, etc.) and I believe all of them were that or slower. 

Maybe I miss something
1578570173380001799
RT @eu_Robotz: tweepy é incrível kkkk

#bolhadev
1578569922942308361
2022-10-08 02:16:12.637185 tweepy
1578569419638423560
2022-10-08 02:14:12.636719 tweepy
1578568916317753344
2022-10-08 02:12:12.640027 tweepy
1578568413055787008
2022-10-08 02:10:12.638372 tweepy
1578568042509893633
RT @eu_Robotz: tweepy é incrível kkkk

#bolhadev
1578568020800462849
tweepy é incrível kkkk

#bolhadev
1578567909726642177
2022-10-08 02:08:12.636561 tweepy
```

2. Gey my account:
```
client = tweepy.Client(bearer_token)

# Get Users

# This endpoint/method returns a variety of information about one or more users
# specified by the requested IDs or usernames

user_ids = [1408690808128114691]

# By default, only the ID, name, and username fields of each user will be
# returned
# Additional fields can be retrieved using the user_fields parameter
response = client.get_users(ids=user_ids, user_fields=["profile_image_url"])

for user in response.data:
    print(user.username, user.profile_image_url)
```
Result, that is my user name and my portrait:
```
aCatotea https://pbs.twimg.com/profile_images/1408691247129063432/Obl2DgFq_normal.jpg
```
