import numpy as np
import matplotlib.pylab as pyl

def relu(x):
    return np.maximum(0,x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)

pyl.plot(x,y)
pyl.ylim(-0.1, 6.0)
pyl.show()
