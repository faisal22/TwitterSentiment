# # from ggplot import *
# # from multiprocessing import Process
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import time
# # from threading import Thread
# # import random

# # class MyThread (Thread):

# #     def __init__(self, thread_id):
# #         Thread.__init__(self)
# #         self.thread_id = thread_id
# #         print('init')

# #     def run(self):
# #     	time.sleep(5)
# #     	counter = 0
# #     	while True:
# #     		i = random.uniform(1,9)
# #     		i_y = random.uniform(1,9)
# #     		plt.scatter(i,i_y)
# #     		counter = counter + 1	
# #     		if(counter == 4):
# #     			plt.draw()
# #     			counter = 	0 


# # def main():
# # 	thread1 = MyThread(1)
# # 	thread1.daemon = True
# # 	# while(True):
# # 		# print 'in thread\n'
# # 		# plt.ion()
	

# # 	# plt.scatter(x, y)

# # 	# plt.ion()
# # 	# plt.show()
# # 	# plt.draw()
# # 	# thread1.start()


# # 		# print 'after thread\n'
# # 	# print 'hi'
# # 	# for i in range(3):
# # 		# time.sleep(5)
# # 		# print 'hi'

# # main()

from SentimentGraph import SentimentGraph

sg = SentimentGraph()
sg.setProperties()
sg.plot(6,6, 'ushnaha is the loserst loser of all times')
sg.startGraph()

# class FollowDotCursor(object):

# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = plt.axes()


# points_with_annotation = []
# for i in range(10):
#     point, = plt.plot(i, i, 'o', markersize=10)

#     annotation = ax.annotate("Mouseover point %s" % i,
#         xy=(i, i), xycoords='data',
#         xytext=(i, i+0.2), textcoords='data',
#         horizontalalignment="left",
#         bbox=dict(boxstyle="round", facecolor="w", 
#                   edgecolor="0.5", alpha=0.9)
#         )
#     # by default, disable the annotation visibility
#     annotation.set_visible(False)

#     points_with_annotation.append([point, annotation])


# def on_move(event):
# 	print 'on_move'
# 	print event

#     # visibility_changed = False
#     # for point, annotation in points_with_annotation:
#     #     should_be_visible = (point.contains(event)[0] == True)

#     #     if should_be_visible != annotation.get_visible():
#     #         visibility_changed = True
#     #         annotation.set_visible(should_be_visible)

#     # if visibility_changed:        
#     #     plt.draw()

# on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)

# plt.show()