import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

mat_file = sio.loadmat('matlab.mat')

list_obstacles = mat_file['X']

x = []
y = []

for i in range(len(list_obstacles)):
	x.append(list_obstacles[i][0])
	y.append(list_obstacles[i][1])

"""
plt.plot(x,y,'ro')
plt.show()
"""

x_axis = np.arange(-6, 2, 0.1)
y_axis = np.arange(8, 0, 0.1)

grid = [[0 for ys in range(80)] for xs in range(1)]
counter = 0
for xs in range(1,80):
	for ys in range(1,80):
		for j in range(len(y)):
			for i in range(len(x)):
				counter += 1
				print counter
				if x[i] >= x_axis[xs-1] and x[i] <= x_axis[xs] and y[j] >= y_axis[ys-1] and y[j] <= y_axis[ys]:
					grid[xs][ys] = 1
					
print grid