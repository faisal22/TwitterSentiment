#imports
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json,sys,datetime,os,time,traceback
import numpy as np
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from TweetHandler import TweetHandler
from Tweet import Tweet
from threading import Thread

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
	def __init__(self, outputfile, sentimentGraph):
		self.output_stream =  outputfile
		# We load in the list of words and their log probabilities
		# self.happy_log_probs, self.sad_log_probs = readSentimentList('twitter_sentiment_list.csv')
		self.tweetHandler = TweetHandler(sentimentGraph)

	def on_data(self, data):
		try:
			keys = json.loads(data).keys()
			if('text' in keys and 'created_at' in keys):
				tweet_raw = json.loads(data)['text']

				created_at = json.loads(data)['created_at']

				self.tweetHandler.handleTweet(tweet_raw)
				# t = Tweet(tweet_raw)
				# t.compute()

				# self.sentimentGraph.plot(t.getValence(), t.getArousal(), tweet_raw)

				# print "["+created_at +"]\t" +tweet_raw+"\n"

	 			# blob = TextBlob(tweet, analyzer=NaiveBayesAnalyzer())
				# self.output_stream.write("["+created_at +"]\t" +tweet_raw +"\n")# +str(blob.sentiment) +"\n\n")
				# self.output_stream.flush()
		except UnicodeEncodeError as uee:
			None
		return True

	def on_error(self, status):
		print status
		return False


class TweetConnection():
	def __init__(self, sentimentGraph):

		print('initializing connection variables.....'),
		#setting up the keys
		self.consumer_key 	= 'euSriOE9VFoHkbC0ZiXGgKkN4'
		self.consumer_secret = 'iB791h3YZP60dDoKPVcj0HKNGKCVoG1aYapUZd8rIK5ozSMoLs'
		self.access_token 	= '179897744-aUOSCU3B77TnnDGkKOoyvPn5KKYbMStZTaT9o2Jb'
		self.access_secret 	= 'aDSsCFIFhY3iUpvuGDHNX30FRQXI3GqssfaN7Wh2gGgNI'
		self.sentimentGraph = sentimentGraph

		# http://boundingbox.klokantech.com/
		self.USA_LOCATIONS = [-125.18,25.52,-58.94,48.98]
		self.FEEL_WORDS = ['feel', 'makes me', 'I\'m', 'I am', 'im', 'i am', 'feeling', 'feelings', 'love', 'hate', 'anxiety', 'anxious']
		printGreen('successful')
		print('consumer key: '+self.consumer_key)
		print('consumer secret: '+self.consumer_secret)
		print('access token: '+self.access_token)
		print('access secret: '+self.access_secret)
		print('locations to track: '+str(self.USA_LOCATIONS))
		print('words to track: '+str(self.FEEL_WORDS))

	def initAuth(self):
		print('authorizing.....'),
		self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_secret)
		printGreen('successful')

	def initLogDir(self):
		print('initializing log directory.....'),
		now = datetime.datetime.now()
		self.LOG_DIRNAME		= '.\\logs\\'
		self.LOG_FILENAME 	= 'twitterdata' +str(now.year) +str(now.month) +str(now.day) +str(now.hour) +str(now.minute) +'.data'
		if not os.path.exists(self.LOG_DIRNAME):
			os.makedirs(self.LOG_DIRNAME)
		printGreen('successful')

	def start(self):
		while True:	
			try:		
				stream = Stream(self.auth, TweetListener(open(self.LOG_DIRNAME+self.LOG_FILENAME, 'w'), self.sentimentGraph))
				stream.filter(locations =  self.USA_LOCATIONS, track = self.FEEL_WORDS)
			except KeyboardInterrupt as e:
				sys.exit()	
			except Exception as ex:
				traceback.print_exc(file=sys.stdout)
			printRed('something happened. going to sleep.')	
			time.sleep(5)
			printRed('creating Stream object...')

# http://en.wikipedia.org/wiki/ANSI_escape_code
def printRed(text):
	CSI="\x1B["
	print CSI+"31;40m" +text + CSI + "0m"

def printGreen(text):
	CSI="\x1B["
	print CSI+"32;40m" +text + CSI + "0m"	

class TweetConnectionThread(Thread):

	def __init__(self, sentimentGraph):
		self.sentimentGraph = sentimentGraph
		Thread.__init__(self)

	def run(self):
		try:
			tc = TweetConnection(self.sentimentGraph)
			tc.initAuth()
		except Exception as e:
			printRed('failed')
			print e
			sys.exit()
		try:
			tc.initLogDir()
		except Exception as e:
			printRed('failed')
			print e
			sys.exit()
		s = raw_input('\npress enter to continue.....')
		if(len(s)==0):
			print 'starting stream.....\n'
			tc.start()
