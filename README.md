# Examples

```
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

Send = Scheduled.send(message="Test")
print(Send)
```