import prm
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from collision_tester import convert_coords

#y = prm.lis
"""
x = np.array([0,1,2,3,4,5,6,7,6,5,4,3,2,1,0])
y = np.array([0,1,2,3,4,4,5,6,7,8,7,8,9,9,9])"""
#x = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,6,5,4,3,2,1,0])
#y = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4,4,4.5,5,5.5,6,7,8,7,8,9,9,9])
x = np.array([0,1,2,3,4,5,6,7,8])
#y = np.array([0,1,2,3,4,4,5,6,9])
y = np.array([9,9,9,8,7,8,7,6,5])
"""
print convert_coords(0,0,1,1)

x = np.linspace(0, 70, num = 8, endpoint = True)
#x = np.insert(x, 8, [6,5,4,3,2,1,0])
print x
#x = np.insert(x, [7,8,9,10,11,12,13], [6,5,4,3,2,1,0])
y = prm.lis
for i in range(0,len(y)):
	y[i] = float(y[i])
y = y[0:8]
print y
"""
f = interp1d(x, y)
f2 = interp1d(x, y, kind = 'cubic')

xnew = np.linspace(0, 7, num = 100, endpoint = True)

plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc = 'best')
plt.show()