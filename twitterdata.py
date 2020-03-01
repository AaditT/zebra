import tweepy
import csv
import sys


from creds import consumer_key, consumer_secret, access_key, access_secret


twitter_handles = {
    "klobuchar" : "amyklobuchar",
    "sanders" : "BernieSanders",
    "biden" : "JoeBiden",
    "warren" : "ewarren",
    "buttigeig" : "PeteButtigieg",
    "bloomberg" : "MikeBloomberg",
    "gabbard" : "TulsiGabbard",
    "weld" : "GovBillWeld",
    "trump" : "realDonaldTrump",
    "de_la_fuente" : "JoinRocky",

}

def get_all_tweets(screen_name, num):
    num = int(num)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    alltweets = []
    try:
        new_tweets = api.user_timeline(screen_name = screen_name,count=1)
    except:
        raise Exception("Twitter user " + screen_name + " does not exist!")
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0 and len(new_tweets) < int(num):
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

    outtweets = []

    for tweet in alltweets:
        try:
            pass
            # print(tweet.text)
        except (NameError, KeyError):
            pass
        else:
            outtweets.append(tweet.text)
    outtweets = outtweets[:num]
    return outtweets
