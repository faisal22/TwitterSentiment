import matplotlib.pyplot

class SentimentGraph:

	def __init__(self):
		self.plt = matplotlib.pyplot	

		self.fig = self.plt.figure()
		self.ax 		 = self.plt.axes()

		on_move_id = self.fig.canvas.mpl_connect('motion_notify_event', self.on_move)
		self.points_with_annotation = []

	def setProperties(self):
		self.plt.axhline(y=5, color = 'black', linewidth = 3)
		self.plt.axvline(x=5, color = 'black', linewidth = 3)
		self.plt.grid(True)
		self.plt.axis([1,9,1,9])
		self.plt.text(1, 5, 'Unpleasant', bbox={'facecolor':'red', 'alpha':0.5})

		self.plt.text(1.8, 7, 'Upset', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(2.6, 8.2, 'Stressed', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(3.4, 8.6, 'Nervous', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(4.2, 8.82, 'Tense', bbox={'facecolor':'red', 'alpha':0.5})

		self.plt.text(4.8, 8.85, 'Activation', bbox={'facecolor':'red', 'alpha':0.5})

		self.plt.text(5.8, 8.82, 'Alert', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(6.6, 8.6, 'Excited', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(7.4, 8.2, 'Elated', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(8.2, 7.4, 'Happy', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(8.7, 5, 'Pleasant', bbox={'facecolor':'red', 'alpha':0.5})

		self.plt.text(1.8, 3, 'Sad', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(2.8, 1.66, 'Depressed', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(3.7, 1.2, 'Bored', bbox={'facecolor':'red', 'alpha':0.5})

		self.plt.text(4.8, 1.10, 'Deactivation', bbox={'facecolor':'red', 'alpha':0.5})

		self.plt.text(5.8, 1.18, 'Calm', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(6.6, 1.4, 'Relaxed', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(7.4, 1.8, 'Serene', bbox={'facecolor':'red', 'alpha':0.5})
		self.plt.text(8.2, 2.6, 'Contented', bbox={'facecolor':'red', 'alpha':0.5})

	def startGraph(self):
		self.plt.show(block=True) #this cause the mainloop

	def plot(self, x, y, tweet_raw):
		point = self.plt.scatter(x,y)
		self.plt.draw()

		annotation = self.ax.annotate(tweet_raw, xy=(x,y), xycoords='data', xytext=(x, y+0.2), textcoords='data', horizontalalignment="left", bbox=dict(boxstyle="round", facecolor="w", edgecolor="0.5", alpha=0.7))
	    
		# print annotation

	    # by default, disable the annotation visibility
		annotation.set_visible(False)
		self.points_with_annotation.append([point, annotation])


	def on_move(self, event):
		visibility_changed = False
		for point, annotation in self.points_with_annotation:
		    should_be_visible = (point.contains(event)[0] == True)

		    if should_be_visible != annotation.get_visible():
		        visibility_changed = True
		        annotation.set_visible(should_be_visible)

			# if visibility_changed:        
			# 	self.plt.draw()



# def main():
# 	g = SentimentGraph()
# 	g.setProperties()
# 	g.plot(4,7)
# 	g.startGraph()


# main()