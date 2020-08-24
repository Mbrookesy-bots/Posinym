import tweepy
import json

#Gather data from config file for authentication
with open("../config.json", "r") as file:
    config = json.load(file)

auth = tweepy.OAuthHandler(config["consumerApiKey"], config["consumerApiSecretKey"])
auth.set_access_token(config["authApiKey"], config["authApiSecret"])

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

print(api.verify_credentials())