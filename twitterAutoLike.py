import tweepy

APIKEY = ""
APIKEYSECRET = ""
ACCESSTOKEN = ""
ACCESSTOKENSECRET = ""

""" 認証準備 """
auth = tweepy.OAuthHandler(APIKEY, APIKEYSECRET)
auth.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)

api = tweepy.API(auth)

""" Tweet取得 """
tweets = api.search_tweets(q="プログラミング", result_type="recent", count=5)
#print(objects)

for tweet in tweets:
    try:
        favoriteId = tweet.id
        api.create_favorite(favoriteId)
        print("Like text is: " + tweet.text)

    except tweepy.TweepyException as e:
        print(e)
