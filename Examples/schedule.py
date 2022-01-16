from ScheduleTweet import TweetClient
import asyncio

bearer_token = "XXXXXXXXXX"
consumer_key = "XXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXX"

Tweet = TweetClient(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token,
)


async def schedule_tweet():
    print(await Tweet.data())
    Send = await TweetClient.schedule_send(message="Wow, cool!", timer="20:40")
    print(Send)


asyncio.run(schedule_tweet())
