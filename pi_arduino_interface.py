#from get_path import out, xys, array
import numpy as np
import matplotlib.pyplot as plt

input_array = []
bot_location = [0, 0, 0]

def move(input_array):
	pass

def slice_array(xy_array):
	counter = 0
	for i in range(len(xy_array[0])):
		counter += 1
		if xy_array[0][i] == 0.0:
			break
	xy_array[0] = xy_array[0][0:counter-1]
	xy_array[1] = xy_array[1][0:counter-1]
	#print xy_array
	return xy_array

def find_displacement(xy_array):
	bot_location = [0, 0, 0]
	xy_array = slice_array(xy_array)
	px = [0]
	py = [0]
	pt = [0]
	pd = [0]
	for i in range(1, len(xy_array[0])):
		x = xy_array[0][i]
		y = xy_array[1][i]

		#print x, y

		theta = np.arctan((y - bot_location[1])/(x - bot_location[0]))
		theta_deg = 180/np.pi * theta
		#print theta_deg
		d = abs((x - bot_location[0])/np.cos(theta))
		pd.append(d)

		input_array = [d, theta]
		
		#print input_array
		bot_location = [x, y, theta]
		px.append(x)
		py.append(y)

		move(input_array)
		#print bot_location
		#print input_array
	plt.plot(px, py)
	#plt.axis([0, 10, 0, 10])
	plt.show()

#find_displacement(out)