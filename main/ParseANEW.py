import csv
class ParseANEW:
	def __init__(self):
		self.anewDictionary = {}

	def parse(self, anew):
		reader = csv.DictReader(open(anew, 'rb'), delimiter=',')
		for line in reader:
			key = line['description-word']
			self.anewDictionary[key] = {'valence-mean': float(line['valence-mean']),'valence-SD': float(line['valence-SD']),'arousal-mean':float(line['arousal-mean']),'arousal-SD': float(line['arousal-SD']),'dominance-mean':float(line['dominance-mean']),'dominance-SD': float(line['dominance-SD']),'word-freq': float(line['word-freq'])}

	def getValence(self, word):
		v_stats = []

		if not self.anewDictionary.get(word) == None:
			v_stat = self.anewDictionary.get(word)
			v_stats.append(v_stat['valence-mean'])
			v_stats.append(v_stat['valence-SD'])
			return v_stats
		return None

	def getArousal(self,word):
		a_stats = []

		if not self.anewDictionary.get(word) == None:
			a_stat = self.anewDictionary.get(word)
			a_stats.append(a_stat['arousal-mean'])
			a_stats.append(a_stat['arousal-SD'])
			return a_stats
		return None