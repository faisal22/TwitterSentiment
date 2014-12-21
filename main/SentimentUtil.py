import re, enchant
from ParseANEW import ParseANEW
from nltk.stem.wordnet import WordNetLemmatizer
from ANEWAnalysis import ANEWAnalysis

class SentimentUtil:

	def __init__(self):
		self.parseAnew = ParseANEW()
		self.parseAnew.parse('anew.csv')
		self.dict 	   = enchant.Dict('en_US')
		self.lmtzr 	   = WordNetLemmatizer()

		self.valenceAnalyzer = ANEWAnalysis()
		self.arousalAnalyzer = ANEWAnalysis()
			# self.rePattern2 = re.compile('[\w]+')

	# @classmethod
	def passTweet(self, tweet_raw):
		tweet_tokens = tweet_raw.split(' ')
		print 'tweet_tokens: '+str(tweet_tokens)
		for i in range(len(tweet_tokens)):
			self.dictFilter(tweet_tokens[i].strip())

		print(self.valenceAnalyzer.computeSentiment())
		print(self.arousalAnalyzer.computeSentiment())

		return 0

	def dictFilter(self, word):
		word = word.lower()
		if(len(word) > 2 and word.isalpha() and self.dict.check(word)):

			
			# stem = self.lmtzr.lemmatize(word)  #comment in line to stem valid words (bogs down speed!)
			stem = word
			v_stats = self.parseAnew.getValence(stem)
			if(v_stats != None):
				self.valenceAnalyzer.addTuple(v_stats[0], v_stats[1])

			a_stats = self.parseAnew.getArousal(stem)
			if(a_stats != None):
				self.arousalAnalyzer.addTuple(a_stats[0], a_stats[1])
			if(a_stats != None and v_stats != None):
				print 'stats found for : '+stem

def main():
	senUtil = SentimentUtil()
	senUtil.passTweet('@NatalieDuvalNY Syrian Regime health	 13 Mourners at win Protest (Video) http://bit.ly/ftjOBU #tcot #Syria #Obama #p2 #IranElection')
main() 
