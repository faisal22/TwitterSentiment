from Queue import Queue
from Tweet import Tweet

class TweetHandler:
	def __init__(self):
		self.tweet_BUFFER = Queue()
	

	def handleTweet(self, tweet_raw):
		t = Tweet(tweet_raw)
		self.tweet_BUFFER.put(t)
		if not self.tweet_BUFFER.empty():
			nextTweet = self.tweet_BUFFER.get()
			self.dispatch(nextTweet)

	def dispatch(self, tweet):
		tweet.compute()
