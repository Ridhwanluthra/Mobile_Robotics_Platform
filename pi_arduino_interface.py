from get_path import out, xys
import numpy as np

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
	xy_array[1] = xy_array[0][0:counter-1]
	print xy_array
	return xy_array

def find_displacement(xy_array):
	bot_location = [0, 0, 0]
	xy_array = slice_array(xy_array)
	for i in range(1, len(xy_array[0])):
		x = out[0][i]
		y = out[1][i]

		theta = np.arctan((y - bot_location[1])/(x - bot_location[0]))
		theta_deg = 180/np.pi * theta
		d = (x - bot_location[0])/np.cos(theta)

		input_array = [d, theta]
		print input_array
		bot_location = [x, y, theta]

		move(input_array)
		#print bot_location
		#print input_array

find_displacement(out)