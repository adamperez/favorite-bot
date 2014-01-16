
from twitter import Twitter, OAuth, TwitterHTTPError

OAUTH_TOKEN = '59980817-6o1KUWI1QIWfYZdyCMSsVXAdWxd3q8ANqlUT4JC11'
OAUTH_SECRET = 'KUZNZ23P3CoAZZsp6IjExBv0iugAP9HsdSdlYkegA9k0v'
CONSUMER_KEY = 'iO7DcWFvPc2ert4TPLeKg'
CONSUMER_SECRET = '45gg8j3awETCkAiAW05u7WOvVWkPsiIqXXPrNUQ4'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#Method that will search twitter for tweets
def search_tweets(q, count=100):
	return t.search.tweets(q=q, result_type='recent', count=count)

#Method to favorite tweet
def fav_tweet(tweet):
	try:
		result = t.favorites.create(_id=tweet['id'])
		print "Favorited: %s" % (result['text'])
		return result
	#if tweet is already favorited
	#throw exception
	except TwitterHTTPError as e:
		print "Error: ", e
		return None

#Method to automatically favorite tweets
def auto_fav(q, count=100):
	result = search_tweets(q, count)
	a = result['statuses'][0]['user']['screen_name']
	print a
	success = 0
	for tweet in result['statuses']:
		if fav_tweet(tweet) is not None:
			success += 1
	print "We favorited a total of %i out of %i tweets" % (success, len(result['statuses']))
