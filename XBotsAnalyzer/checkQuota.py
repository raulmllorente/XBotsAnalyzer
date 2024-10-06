import tweepy
import config

authTweepy = tweepy.OAuthHandler(config.twitter_app_auth['consumer_key'], config.twitter_app_auth['consumer_secret'])
authTweepy.set_access_token(config.twitter_app_auth['access_token'], config.twitter_app_auth['access_token_secret'])
api = tweepy.API(authTweepy)
data = api.rate_limit_status()
print (data['resources']['users']['/users/lookup'])