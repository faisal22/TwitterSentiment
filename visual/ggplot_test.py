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
	

	# plt.scatter(x, y)

	# plt.ion()
	# plt.show()
	# plt.draw()
	# thread1.start()


		# print 'after thread\n'
	# print 'hi'
	# for i in range(3):
		# time.sleep(5)
		# print 'hi'

main()