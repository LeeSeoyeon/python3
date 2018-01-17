import numpy as np
import matplotlib.pylab as pyl

def sigmoid(x):
    return 1/ (1+ np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

pyl.plot(x,y)
pyl.ylim(-0.1, 1.1)
pyl.show()
