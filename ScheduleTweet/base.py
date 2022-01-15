import tweepy
import schedule
from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M:%S")


class TweetClient:
    def __init__(
        self,
        consumer_key: str,
        consumer_secret: str,
        access_token: str,
        access_token_secret: str,
        bearer_token: str,
    ):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.bearer_token = bearer_token

    async def data(self):
        global consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
        consumer_key = self.consumer_key
        consumer_secret = self.consumer_secret
        access_token = self.access_token
        access_token_secret = self.access_token_secret
        bearer_token = self.bearer_token
        return f"Consumer_Key: {consumer_key}, \nConsumer_Secret: {consumer_secret}, \nAccess_Token:  {access_token}, \nAcess_Token_Secret: {access_token_secret}, \nBearer_Token = {bearer_token}"

    async def send_tweet(message: str):
        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )
        client.create_tweet(text=message)
        return f"[ {time} ] - Sended! with messages: " + message
    
    async def schedule_send(message: str, timer: str):
        def da():
            client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            )
            client.create_tweet(text=message)
            print(f"[ {time} ] - Sended! with messages: " + message)

        schedule.every().day.at(timer).do(da)
        while True:
            schedule.run_pending()
