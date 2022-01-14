# Examples

```py
import ScheduleTweet
import asyncio

consumer_key = "1"
consumer_secret = "2"
access_token = "3"
access_token_secret = "4"

Tweet = ClientData(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

async def a1():
    Send = await Scheduled.send(message="Test", hour="13", minute="05")
    print(Send)

asyncio.run(a1())
```