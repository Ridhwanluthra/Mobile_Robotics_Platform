import numpy as np

state = [0,0,np.pi/4]

#distance = 10
"""
state[0] = state[0] + distance * np.cos(state[2])
state[1] = state[1] + distance * np.sin(state[2])
"""
distance1 = (7.07 - state[0])/np.cos(state[2])
distance2 = (7.07 - state[1])/np.sin(state[2])
#state[0] = state[0] + distance * np.cos(state[2])
#state[1] = state[1] + distance * np.sin(state[2])

print distance1 , distance2

"""
def forward(distance):
	state[0] = state[0] + distance * np.cos(state[2])
	state[1] = state[1] + distance * np.sin(state[2])

	pass

def turn_left(degrees):
	pass

def turn_right(degrees):
	pass

"""