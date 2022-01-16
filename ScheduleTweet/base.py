import tweepy
import schedule
from datetime import datetime
from typing import Optional
import json

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
        Json = {
            "TweetClient Data Information": {
                "Consumer_Key": f"{self.consumer_key}",
                "Consumer_Secret": f"{self.consumer_secret}",
                "Access_Token": f"{self.access_token}",
                "Access_Token_Secret": f"{self.access_token_secret}",
                "Bearer_Token": f"{self.bearer_token}",
            }
        }
        return f"{json.dumps(Json, indent=4)}"

    async def send_tweet(self, message: str):
        """
        Currently using Twitter API v2
        """
        client = tweepy.Client(
            bearer_token=self.bearer_token,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret,
        )
        client.create_tweet(text=message)
        return f"[ {time} ] - Sended! with messages: " + message

    async def send_tweet_media(
        self, message: str, media: str, media_2: Optional[str] = None
    ) -> str:
        """
        Currently using Twitter API Elevated Access
        """
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        data = api.media_upload(media)

        client = tweepy.Client(
            bearer_token=self.bearer_token,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret,
        )

        if not media_2:
            client.create_tweet(text=message, media_ids=[data.media_id_string])
        return f"Information of the media uploaded: \nMediaID: {str(data.media_id)} \nMedia Size: {str(data.size)} \nMedia Type: {str(data.image['image_type'])}"

    async def schedule_send(self, message: str, timer: str):
        def da():
            client = tweepy.Client(
                bearer_token=self.bearer_token,
                consumer_key=self.consumer_key,
                consumer_secret=self.consumer_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
            )
            client.create_tweet(text=message)
            print(f"[ {time} ] - Sended! with messages: " + message)

        schedule.every().day.at(timer).do(da)
        while True:
            schedule.run_pending()
