from pylab import *
import matplotlib.mlab as mlab
import sys

class ANEWAnalysis:
	def __init__(self):
		self.means 	= []
		self.sds 	= []
		self.p_vals	= []
		self.sentiment = None

		self.NORM_LOW = 1
		self.NORM_HI = 9
	
	def addTuple(self, mean, sd):
		self.means.append(mean)
		self.sds.append(sd)

		p = mlab.normpdf(mean,mean,sd)
		self.p_vals.append(p)
		
	def computeSentiment(self):

		# print self.means, self.sds,self.p_vals

		if self.sentiment == None:
			weights = []
			p_sum	= sum(self.p_vals)

			for i in range(len(self.p_vals)):
				weights.append(self.p_vals[i]/p_sum)
			
			# print weights

			self.sentiment = 0
			for i in range(len(weights)):
				self.sentiment += (weights[i] * self.means[i])

	def getSentiment(self):
		if self.sentiment == None:
			self.computeSentiment()

		if self.sentiment != None:
			return self.sentiment

	def getNormalizedSentiment(self):
		sentiment = self.getSentiment()
		return sentiment
		# return (sentiment - self.NORM_LOW)/(self.NORM_HI-self.NORM_LOW)

