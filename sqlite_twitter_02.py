import twitter
import json
import sqlite3

def oauth_login():
    # XXX: Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://dev.twitter.com/docs/auth/oauth for more information 
    # on Twitter's OAuth implementation.
    
    CONSUMER_KEY = 'QWxBzzr1r55FN7ZlyxFg1VgeG'
    CONSUMER_SECRET = 'ezDbcIStUkogt9ijnJfCGsFbz8wVc2p4VKBmBLXTODzjpoId55'
    OAUTH_TOKEN = '2805580770-TKHgMmd8jtuEpNBd1JbzducTifZfhZdUlF97U3z'
    OAUTH_TOKEN_SECRET = 'vENMVaRYYXYf1n4mvXeEJcoVPMae7PCMUim8uEEPQmi1q'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# Sample usage
twitter_api = oauth_login()    


# Code taken from: Mining the Social Web, 2nd Edition (O'Reilly)


conn = sqlite3.connect("c:/data/trending.sqlite")
c = conn.cursor()

def twitter_trends(twitter_api, woe_id):
    # Prefix ID with the underscore for query string parameterization.
    # Without the underscore, the twitter package appends the ID value
    # to the URL itself as a special-case keyword argument.
    return twitter_api.trends.place(_id=woe_id)



MANC_WOE_ID = 28218
manc_trends = twitter_trends(twitter_api, MANC_WOE_ID)
manc = json.dumps(manc_trends)

manc = json.loads(manc)


for x in manc:
    locs = x["locations"]
    trends = x["trends"]
    timestamp =  x["created_at"]
    
for loc in locs:
    name = loc["name"] 
    woeid = loc["woeid"]
    woeid = int(woeid)
for trend in trends:
    query = trend["name"] 
    url = trend["url"] 
    tweet_volume = trend["tweet_volume"]
    if str(tweet_volume) == 'None':
        tweet_volume = 0
    else :
        tweet_volume = int(str(tweet_volume))
    c.execute("INSERT INTO trends VALUES (?, ?, ?, ?, ?, ?);", (timestamp, woeid, name, url, tweet_volume, query  ))
    conn.commit()
