#imports
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json,sys,datetime,os
import numpy as np
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from TweetHandler import TweetHandler

#setting up the keys
consumer_key 	= 'euSriOE9VFoHkbC0ZiXGgKkN4'
consumer_secret = 'iB791h3YZP60dDoKPVcj0HKNGKCVoG1aYapUZd8rIK5ozSMoLs'
access_token 	= '179897744-aUOSCU3B77TnnDGkKOoyvPn5KKYbMStZTaT9o2Jb'
access_secret 	= 'aDSsCFIFhY3iUpvuGDHNX30FRQXI3GqssfaN7Wh2gGgNI'

def readSentimentList(file_name):
	ifile = open(file_name, 'r')
	happy_log_probs = {}
	sad_log_probs = {}
	ifile.readline() # Ignore title row

	for line in ifile:
		tokens = line[:-1].split(',')
		happy_log_probs[tokens[0]] = float(tokens[1])
		sad_log_probs[tokens[0]] = float(tokens[2])

	return happy_log_probs, sad_log_probs
     
def classifySentiment(words, happy_log_probs, sad_log_probs):

	# Get the log-probability of each word under each sentiment
	happy_probs = [happy_log_probs[word] for word in words if word in happy_log_probs]
	sad_probs = [sad_log_probs[word] for word in words if word in sad_log_probs]

	# Sum all the log-probabilities for each sentiment to get a log-probability for the whole tweet
	tweet_happy_log_prob = np.sum(happy_probs)
	tweet_sad_log_prob = np.sum(sad_probs)

	# Calculate the probability of the tweet belonging to each sentiment
	prob_happy = np.reciprocal(np.exp(tweet_sad_log_prob - tweet_happy_log_prob) + 1)
	prob_sad = 1 - prob_happy	

	return prob_happy, prob_sad

class TweetListener(StreamListener):

	# A listener handles tweets are the received from the stream.
	#This is a basic listener that just prints received tweets to standard output
	def __init__(self, outputfile):
		self.output_stream =  outputfile
		# We load in the list of words and their log probabilities
		# self.happy_log_probs, self.sad_log_probs = readSentimentList('twitter_sentiment_list.csv')
		self.tweetHandler = TweetHandler()

	def on_data(self, data):
		try:
			tweet_raw = json.loads(data)['text']
			# created_at = json.loads(data)['created_at']
			self.tweetHandler.handleTweet(tweet_raw)

			# print "["+created_at +"]\t" +tweet +"\n"
			# blob = TextBlob(tweet, analyzer=NaiveBayesAnalyzer())
			# self.output_stream.write("["+created_at +"]\t" +tweet +"\n")# +str(blob.sentiment) +"\n\n")
			# self.output_stream.flush()
		except Exception as ex:
			print ex
		return True

	def on_error(self, status):
		print status

	def __getattr__(self, attr):
         return getattr(output_stream, attr)

def start_stream():
	now = datetime.datetime.now()
	LOG_DIRNAME		= '.\\logs\\'
	LOG_FILENAME 	= 'twitterdata' +str(now.year) +str(now.month) +str(now.day) +str(now.hour) +str(now.minute) +'.data'
	if not os.path.exists(LOG_DIRNAME):
		os.makedirs(LOG_DIRNAME)
	
	while True:
		try:		
			stream = Stream(auth, TweetListener(open(LOG_DIRNAME+LOG_FILENAME, 'w')))
			stream.filter(locations =  USA_LOCATIONS, track = FEEL_WORDS)
		except KeyboardInterrupt as e:
			sys.exit()		
		except Exception as ex:
			print ex
			continue

#	http://boundingbox.klokantech.com/
USA_LOCATIONS = [-125.18,25.52,-58.94,48.98]
FEEL_WORDS = ['feel', 'makes me', 'I\'m', 'I am', 'im', 'i am', 'feeling', 'feelings', 'love', 'hate', 'anxiety', 'anxious']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
start_stream()