import tweepy
import time

#copy below four things from Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,,access_token_secret)

api = tweepy.API(auth)
user=api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

def limit_handler(cursor):
   try:
      while True:
      yield cursor.next()
   except tweepy.RateLimitError:
      time.sleep(1000)

#Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
   if follower.name == 'Nnesandz_05':
      follower.follow()
      break

   if followers.followers_count > 100:
      follower.follow()
      break

   print(follower.name)

#Narcissist Bot
search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.cursor(api.search,search_string).items(NumberOfTweets):
   try:
      tweet.favorite()
      tweet.retweet()
      print('I liked that tweet')
   except tweepy.TweepError as e:
      print(e.reason)
   except StopIteration:
      break