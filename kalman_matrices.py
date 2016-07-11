import numpy as np


measurements = [1,2,3,4,5,6,7,8,9,10]
measurement_counter = 0

x = np.matrix([[0.],[0.]])
P = np.matrix([[1000. , 0.],[0. , 1000.]])
u = np.matrix([[0.],[0.]])
F = np.matrix([[1. , 1.],[0. , 1.]])
H = np.matrix([[1. , 0.]])
R = np.matrix([[1.]])
I = np.matrix([[1. , 0.],[0. , 1.]])
y = np.matrix([])
s = np.matrix([])
k = np.matrix([])

global x, P, u, F, H, R, I, measurement_counter, y, s, k

def filter():
	global x, P, u, F, H, R, I, measurement_counter, y, s, k
	update_measurement()
	update_prediction()

	print 'x = ', x
	#print 'P = ', P

def update_measurement():
	global x, P, u, F, H, R, I, measurement_counter, y, s, k
	y = np.mat(measurements[measurement_counter]) - (H * x)
	measurement_counter += 1
	s = (H*P*H.T) + R
	k = (P*H.T)*s.I
	x = x + (k*y)
	P = (I - k*H)*P

def update_prediction():
	global x, P, u, F, H, R, I, measurement_counter, y, s, k
	x = F * x + u
	P = F * P * F.T

while measurement_counter <= 9:
	filter()