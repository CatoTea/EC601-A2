import tweepy

# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKi4hwEAAAAASOZYxep%2BbEf81S%2FnhgVYxtbHhtE%3DZcqa24AEsBUWJ10H4Mda78Y5V5c2O5RMR0DOCSBow8pwEVJBcK"


client = tweepy.Client(bearer_token)

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

response = client.search_recent_tweets("Tweepy")
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

tweets = response.data

for tweet in tweets:
    print(tweet.id)
    print(tweet.text)

##############

user_ids = [1408690808128114691] # user: aCatofTea

# By default, only the ID, name, and username fields of each user will be
# returned
# Additional fields can be retrieved using the user_fields parameter
response = client.get_users(ids=user_ids, user_fields=["profile_image_url"])

for user in response.data:
    print(user.username, user.profile_image_url)
