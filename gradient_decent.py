"""
h = a + b*x

for i in 

j = 
"""
import numpy as np
import random
import pylab


def gradient_descent(alpha, x, y, numIterations):
    m = len(x) # number of samples
    theta = np.ones(2)
    x_transpose = x.transpose()
    for iter in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        J = np.sum(loss ** 2) / (2 * m)  # cost
        print "iter %s | J: %.3f" % (iter, J)      
        gradient = np.dot(x_transpose, loss) / m         
        theta = theta - alpha * gradient  # update
    return theta

x = np.arange(10, 200)
x = np.transpose(x)
y = np.arange(20, 210)

for i in range(len(y)):
	a = y[i] - 5
	b = y[i] + 5
	y[i] = random.uniform(a,b)

m = len(x)
x = np.c_[ np.ones(m), x] # insert column
alpha = 0.00004 # learning rate
theta = gradient_descent(alpha, x, y, 1000000)

# plot
for i in range(x.shape[1]):
    y_predict = theta[0] + theta[1]*x 
pylab.plot(x[:,1],y,'o')
pylab.plot(x,y_predict,'k-')
pylab.show()
print "Done!"