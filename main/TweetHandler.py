from Queue import Queue
from Tweet import Tweet

class TweetHandler:
	def __init__(self, sentimentGraph):
		self.tweet_BUFFER = Queue()
		self.sentimentGraph = sentimentGraph
	

	def handleTweet(self, tweet_raw):
		t = Tweet(tweet_raw)
		self.tweet_BUFFER.put(t)
		if not self.tweet_BUFFER.empty():
			nextTweet = self.tweet_BUFFER.get()
			self.dispatch(nextTweet)

	def dispatch(self, tweet):
		tweet.compute()
		self.sentimentGraph.plot(tweet.getValence(), tweet.getArousal(), tweet.getRaw())
