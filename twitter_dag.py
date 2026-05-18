import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():
    # Twitter API credentials
    consumer_key = 'YFLFLCN2gGHPD0c3pn0kNCn9O'
    consumer_secret = 'N83lAHwI4IVoFzRdiJRD4dFMo3FZRA9RYbpZbbhoJ2l6WMaK1R'
    access_token = '2012575223879528449-0cmePJwOURv2Z2UdOr5M8uxBwCV0ZV'
    access_token_secret = '8a4D2qNzzrWWHvNKFNlEeaKQ3S4BiTdepvKY6c0c6EQhp'

    # Twitter authentication
    auth = tweepy.OAuth1UserHandler(
        consumer_key,
        consumer_secret
    )

    auth.set_access_token(
        access_token,
        access_token_secret
    )

    api = tweepy.API(auth)

    tweets = api.user_timeline(
        screen_name='elonmusk',
        include_rts=False,
        count=200,
        tweet_mode='extended'
    )

    tweet_list = []

    for tweet in tweets:

        text = tweet._json["full_text"]

        refined_tweet = {
            "user": tweet.user.screen_name,
            "text": text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at
        }

        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv('s3://vibhi-airflow/elonmusk_twitter_data.csv', index=False)
