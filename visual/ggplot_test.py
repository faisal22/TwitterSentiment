from ggplot import *
from multiprocessing import Process
import numpy as np
import matplotlib.pyplot as plt
import time
from threading import Thread
import random

class MyThread (Thread):

    def __init__(self, thread_id):
        Thread.__init__(self)
        self.thread_id = thread_id
        print('init')

    def run(self):
    	time.sleep(5)
    	counter = 0
    	while True:
    		i = random.uniform(1,9)
    		i_y = random.uniform(1,9)
    		plt.scatter(i,i_y)
    		counter = counter + 1	
    		if(counter == 4):
    			plt.draw()
    			counter = 	0 


def main():
	thread1 = MyThread(1)
	thread1.daemon = True
	# while(True):
		# print 'in thread\n'
		# plt.ion()
	plt.axhline(y=5, color = 'black', linewidth = 3)
	plt.axvline(x=5, color = 'black', linewidth = 3)
	plt.grid(True)
	plt.axis([1,9,1,9])
	plt.text(1, 5, 'Unpleasant', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(1.8, 5.8, 'Upset', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(2.6, 6.6, 'Stressed', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(3.4, 7.4, 'Nervous', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(4.2, 8.2, 'Tense', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(4.8, 9, 'Activation', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(5.8, 8.2, 'Alert', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(6.6, 7.4, 'Excited', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(7.4, 6.6, 'Elated', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(8.2, 5.8, 'Happy', bbox={'facecolor':'red', 'alpha':0.5})
	plt.text(8.7, 5, 'Pleasant', bbox={'facecolor':'red', 'alpha':0.5})
	# plt.scatter(x, y)

	# plt.ion()
	# plt.show()
	# plt.draw()
	# thread1.start()
	print 'plt.show'
	plt.show(block=True) #this cause the mainloop


		# print 'after thread\n'
	# print 'hi'
	# for i in range(3):
		# time.sleep(5)
		# print 'hi'

main()