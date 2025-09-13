import tweepy
import pandas as pd
import json
import time
from datetime import datetime
import s3fs

access_key="MdYqoFKuMV7J8yvVzUAxhBHiS"
access_secret="eRwKkqS72TniaHqFkJ04275ZYX2jD5ut3fvwZQywZUYbwIrNIb"
consumer_key="1966868571809558528-yTJhK8flQBHZOm1MLQAv7vb5O1XQeL"
consumer_secret="JRhBndsMNlIMzNKLucrtunYStTG0403CZsYahd1QeAjXS"

auth=tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_secret)

api=tweepy.API(auth)
#tweets=api.user_timeline(screen_name='@elonmusk',count=200,include_rts=False,tweet_mode='extended')

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAALyp4AEAAAAAZkC7XQwV2QCX4qJ8dlP72LaSbSQ%3DxRUh1upQoEV2g8yogq3WpOlGmNWVvsJavbhGTkCNaPGZLmCQvy')

user = client.get_user(username='elonmusk')
try:
    tweets = client.get_users_tweets(user.data.id, max_results=100,tweet_fields=['created_at'])
    filtered_tweets = [tweet for tweet in tweets.data if not tweet.text.startswith('RT')]

    for tweet in filtered_tweets:
        print(tweet.text)

except tweepy.TooManyRequests as e:
    print("Rate limit reached. Waiting before retrying...")
    time.sleep(900)
