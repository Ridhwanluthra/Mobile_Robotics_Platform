"""import matplotlib.pyplot as plt
"""
"""
points = [
    (0, 10),
    (10, 20),
    (20, 40),
    (60, 100),
]

x = map(lambda x: x[0], points)
y = map(lambda x: x[1], points)
"""
"""
#plt.rc('grid', linestyle="-", color='black')
x = 0.35
y = 0.35

plt.scatter(x, y)
plt.grid(True)
plt.show()
"""

import numpy as np                                                               
import matplotlib.pyplot as plt                                                                                                                                 

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# major ticks every 20, minor ticks every 5                                      
major_ticks = np.arange(0, 350, 35)
minor_ticks = np.arange(0, 350, 35)

ax.set_xticks(major_ticks)                                                       
ax.set_xticks(minor_ticks, minor=True)                                           
ax.set_yticks(major_ticks)                                                       
ax.set_yticks(minor_ticks, minor=True)                                           

# and a corresponding grid                                                       

ax.grid(which='both')                                                            

# or if you want differnet settings for the grids:                               
ax.grid(which='minor', alpha=0.2)                                                
ax.grid(which='major', alpha=0.5)                                                


plt.show()