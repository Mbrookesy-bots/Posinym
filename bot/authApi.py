import json
import logging

import tweepy

logger = logging.getLogger()


def createApi():
    with open("../config.json", "r") as file:
        config = json.load(file)

    auth = tweepy.OAuthHandler(config["consumerApiKey"], config["consumerApiSecretKey"])
    auth.set_access_token(config["authApiKey"], config["authApiSecret"])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
