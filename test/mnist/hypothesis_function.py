import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def step_function(x):
    y = x > 0
    return np.astype(np.int)

def reLu(x):
    return np.maximum(0, x)

def identity_function(x):
    return x

def softmax(x):
    x = np.exp(x)
    return x/np.sum(x)

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t*np.log(y)) / batch_size