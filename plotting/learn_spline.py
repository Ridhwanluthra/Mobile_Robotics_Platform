import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
"""
#x = np.arange(0, 2*np.pi + np.pi/4, 2*np.pi/8)
#y = np.sin(x)

#x = np.array([0,1,2,3,4,5,6,7,6,5,4,3,2,1,0])
#y = np.array([0,1,2,3,4,4,5,6,7,8,7,8,9,9,9])

x = np.array([0,1,2,3,4,5,6,7,8])
y = np.array([0,1,2,3,4,4,5,6,9])
#y = np.array([9,9,9,8,7,8,7,6,5])

tck = interpolate.splrep(x, y, s = 0)

xnew = np.arange(0,8,0.01)
ynew = interpolate.splev(xnew, tck)

plt.figure()
#plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
plt.plot(x, y, 'x', xnew, ynew, '--')
plt.legend(['Linear', 'cubic spline', 'True'])
plt.axis([0, 10, 0, 10])
plt.title('Cubic-spline interpolation')
plt.show()
"""

#t = np.arange(0,1.1,.1)
#x = np.sin(2*np.pi*t)
#y = np.cos(2*np.pi*t)

x = np.array([0,1,2,3,4,5,6,7,6,5,4,3,2,1,0])
y = np.array([0,1,2,3,4,4,5,6,7,8,7,8,9,9,9])

tck, u = interpolate.splprep([x, y], s = 0)
unew = np.arange(0,9,0.03)
print unew
out = interpolate.splev(unew, tck)
fig = plt.figure()
plt.plot(x, y, '--', out[0], out[1])
plt.legend(['Linear', 'cubic spline'])
plt.axis([0, 10, 0, 10])
plt.title('spline of parametrically defined curve')
"""
a = 35
b = 35

plt.scatter(a, b)
plt.grid(True,'dashes',10)
"""




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