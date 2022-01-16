### Installation

```py
pip install git+https://github.com/StawaDev/ScheduleTweet
```

### Examples

This is a simple example how to use ScheduleTweet! More examples can be found in [here!](https://github.com/StawaDev/ScheduleTweet/tree/main/Examples)

```py
import ScheduleTweet
import asyncio

consumer_key = "1"
consumer_secret = "2"
access_token = "3"
access_token_secret = "4"
bearer_token = "5"

Tweet = TweetClient(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token,
)


async def a1():
    print(await Tweet.data())
    Send = await TweetClient.send_tweet(message="Hey Bro.")
    print(Send)


asyncio.run(a1())

async def a2():
        print(await Tweet.data())
        Send = await TweetClient.schedule_send(message="Hello 123456.", timer="20:40")
        print(Send)


asyncio.run(a2())
```