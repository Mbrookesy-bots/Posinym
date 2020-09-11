import tweepy
import logging
from authApi import createApi
from convertStatus import convertToAntonym
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, keywords, sinceId):
    logger.info("Retrieving mentions")
    newSinceId = sinceId
    for tweet in tweepy.Cursor(api.mentions_timeline, sinceId=sinceId).items():
        newSinceId = max(tweet.id, newSinceId)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")
            api.update_status(
                status=convertToAntonym(tweet.text),
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True,
            )
    return newSinceId


def main():
    api = createApi()
    sinceId = 1
    while True:
        sinceId = check_mentions(api, "positive", sinceId)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
