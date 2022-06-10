import tweepy

all_keys = open("twitterkeys", "r").read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]


authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

api.update_status_with_media( "Location of Bill gate*s jet", filename, *, file, possibly_sensitive, in_reply_to_status_id, lat, long, place_id, display_coordinates)
