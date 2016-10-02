import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import search

#array = search.run_lab()
"""
def extract_xy(array):
	x = np.array([], dtype = 'int')
	y = np.array([], dtype = 'int')
	for i in range(len(array)):
		temp = array[i]
		xy = str(temp).zfill(2)
		x = np.append(x, int(xy[0]))
		y = np.append(y, int(xy[1]))
	return [x, y]
"""
def plot_path(list_of_xys, interpolated_path):
	x = list_of_xys[0]
	y = list_of_xys[1]

	fig = plt.figure()
	plt.plot(x, y, '--')#, interpolated_path[0], interpolated_path[1])
	plt.legend(['Linear', 'cubic spline'])
	plt.axis([0, 10, 0, 10])
	plt.title('spline of parametrically defined curve')



	ax = fig.add_subplot(1,1,1)

	# major ticks every 20, minor ticks every 5                                      
	major_ticks = np.arange(0, 10, 1)
	#minor_ticks = np.arange(0, 350, 35)

	ax.set_xticks(major_ticks)                                                       
	#ax.set_xticks(minor_ticks, minor=True)                                           
	ax.set_yticks(major_ticks)                                                       
	#ax.set_yticks(minor_ticks, minor=True)                                           

	# and a corresponding grid                                                       

	ax.grid(which='both')                                                            

	# or if you want differnet settings for the grids:                               
	#ax.grid(which='minor', alpha=0.2)                                                
	#ax.grid(which='major', alpha=0.5)                                                


	plt.show()

def interpolate_path(list_of_xys):
	x = list_of_xys[0]
	y = list_of_xys[1]
	#print x, y

	#x = np.array([0,1,2,3,4,5,6,7,6,5,4,3,2,1,0])
	#y = np.array([0,1,2,3,4,4,5,6,7,8,7,8,9,9,9])

	tck, u = interpolate.splprep([x, y], s = 0.03)
	unew = np.arange(0,9,0.03)
	#print unew
	interpolated_path = interpolate.splev(unew, tck, ext = 1)
	return interpolated_path

#a = interpolate_path(array)
#plot_path(array, a)