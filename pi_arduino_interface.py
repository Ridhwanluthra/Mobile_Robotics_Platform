#from get_path import out, xys, array
import numpy as np
import matplotlib.pyplot as plt
import serial as ser

input_array = []
bot_location = [0, 0, 0]

def move(input_array):
	data = [1]
	string = '1 '
	arduino = ser.Serial('/dev/ttyUSB1', 115200)
	for i in range(len(input_array[0])):
		"""
		data.append(input_array[0][i])
		data.append(input_array[1][i])
		"""
		string += str(input_array[0][i]) + ' '
		string += str(input_array[1][i]) + ' '
	print string
	arduino.write(string)


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
		
		bot_location = [x, y, theta]
		px.append(x)
		py.append(y)
		pd.append(d)
		pt.append(theta_deg)

		#print bot_location
		#print input_array
	plt.plot(px, py)
	#plt.axis([0, 10, 0, 10])
	plt.show()
	return pd, pt

#find_displacement(out)
arr = [[10,20,10,20,10],[10,350,10,350,10]]
move(arr)