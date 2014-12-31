import re, enchant, os
from ParseANEW import ParseANEW
from nltk.stem.wordnet import WordNetLemmatizer
from ANEWAnalysis import ANEWAnalysis

class Tweet:
	def __init__(self, tweet_raw):
		self.parseAnew = ParseANEW()
		self.parseAnew.parse('./main/anew.csv')
		self.dict 	   = enchant.Dict('en_US')
		self.lmtzr 	   = WordNetLemmatizer()
		self.tweet_raw = tweet_raw
		self.numDictWords = 0

		self.valenceAnalyzer = ANEWAnalysis()
		self.arousalAnalyzer = ANEWAnalysis()

			# self.rePattern2 = re.compile('[\w]+')

	# @classmethod
	def compute(self):
		self.tweet_raw = self.tweet_raw.encode('ascii',errors='ignore')
		tweet_tokens = self.tweet_raw.split(' ')
		# print 'tweet_tokens: '+str(tweet_tokens)
		for i in range(len(tweet_tokens)):
			self.dictFilter(tweet_tokens[i].strip())

		if(self.numDictWords>=2):
			self.valenceAnalyzer.computeSentiment()
			self.arousalAnalyzer.computeSentiment()
			print str(self)+'\n'


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
				self.numDictWords = self.numDictWords + 1
				print 'stats found for : '+stem

	def __str__(self):
		return self.tweet_raw +'\nValence: '+str(self.valenceAnalyzer.getNormalizedSentiment()) +' | Arousal: '+str(self.arousalAnalyzer.getNormalizedSentiment())

	def getValence(self):
		return self.valenceAnalyzer.getNormalizedSentiment()

	def getArousal(self):
		return self.arousalAnalyzer.getNormalizedSentiment()


# def main():
# 	t = Tweet('hi my name is faisal')
# 	t.compute()
# 	print t

# main()