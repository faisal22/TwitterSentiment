from pylab import *
import matplotlib.mlab as mlab
import sys

class ANEWAnalysis:
	def __init__(self):
		self.means 	= []
		self.sds 	= []
		self.p_vals	= []
	
	def addTuple(self, mean, sd):
		self.means.append(mean)
		self.sds.append(sd)

		p = mlab.normpdf(mean,mean,sd)
		self.p_vals.append(p)
		
	def computeSentiment(self):

		print self.means, self.sds,self.p_vals
		weights = []
		p_sum	= sum(self.p_vals)

		for i in range(len(self.p_vals)):
			weights.append(self.p_vals[i]/p_sum)
		
		print weights

		sentiment = 0
		for i in range(len(weights)):
			sentiment += (weights[i] * self.means[i])
			
		return sentiment