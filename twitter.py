import tweepy

consumer_key = "l99IkhQOqaM2I8PB9JLUIE3WE"
consumer_secret = "nYHPXrAGxXNtviwzTNMOe9Kbs9vxHjKY3tKISLqkP5HWkBHnWA"
access_token = "1601187831472332800-CykszS9apIbNwWhavL7cXziwO7gIMM"
access_token_secret = "4zV2ZZ2HrGHlu7VK1pfBYoyiFI9CUgizRveA6Q2oloEFH"

# oAuth2_client_id = "STA4R3hNYktVYk5GTUJJV1dLQ3Y6MTpjaQ"
# oAuth2_client_secret = "0r9b5G3lEYd4gn5qfYQR8k3VwRKo3ahkYHafIVN2xr8x9qPUDy"

class Twitter:

   def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
      self.consumer_key = consumer_key
      self.consumer_secret = consumer_secret
      self.access_token = access_token
      self.access_token_secret = access_token_secret
      auth = tweepy.OAuth1UserHandler(
         self.consumer_key,
         self.consumer_secret,
         self.access_token,
         self.access_token_secret
      )
      self.api = tweepy.API(auth)

   def get_timeline(self):
      public_tweets = self.api.home_timeline()
      for tweet in public_tweets:
         print(tweet.text)

   def post_tweet(self):
      # Upload image
      media = self.api.media_upload(filename="game.jpg", chunked=True)
      # printing the information
      print("The media ID is : " + media.media_id_string)
      print("The size of the file is : " + str(media.size) + " bytes")
      # Post tweet with image
      tweet = "game image"
      post_result = self.api.update_status(status=tweet, media_ids=[media.media_id])
      print(post_result)
      return post_result

   def get_last_tweet(self):
      tweets = self.api.user_timeline(user_id="naphthalene_23", count=1)
      tweet = tweets[0]
      return tweet

      