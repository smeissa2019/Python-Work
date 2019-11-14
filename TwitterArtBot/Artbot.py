import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("HXJwIytG3G6L8d7MAbmuVkbR7")
    consumer_secret = os.getenv("yGgw1oJ43EutwInSPifn9U2k4FAIrwrYu82hJzI2OR7wsoaBFK")
    access_token = os.getenv("1194456102529904640-TszAakWUWgP4rzBB0pQZPsMJl9KOok")
    access_token_secret = os.getenv("7DHlXD5gTzV9GCzxZZ4DklPUwoHBt8upELxT7QykFray4")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api