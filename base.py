import tweepy
import schedule
from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M:%S")


class ClientData:
    def __init__(
        self,
        consumer_key: str,
        consumer_secret: str,
        access_token: str,
        access_token_secret: str,
    ):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def data(self):
        global consumer_key, consumer_secret, access_token, access_token_secret
        consumer_key = self.consumer_key
        consumer_secret = self.consumer_secret
        access_token = self.access_token
        access_token_secret = self.access_token_secret


class TweetClient:
    def setup():
        setup = tweepy.OAuthHandler(
            consumer_key=consumer_key, consumer_secret=consumer_secret
        )
        setup.set_access_token(access_token, access_token_secret)

    def send_tweet(message: str) -> None:
        SendTweet = tweepy.API(TweetClient.setup())
        SendTweet.update_status(status=message)


class Scheduled:
    def send(message: str) -> None:
        schedule.every().day.at("07:15").do(TweetClient.send_tweet(message=message))
        return f"[ {time} ] - Sended!"
