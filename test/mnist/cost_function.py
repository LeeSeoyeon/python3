import numpy as np
from hypothesis_function import softmax, cross_entropy_error

def gradient_desecent_nouse(theta, x, y, lr):
    thetaT = np.transpose(theta)
    value = 1
    lr = 0.1
    h = 0.0001

    #계산이 일차 다항시에서만 오른 계산법이다.
    while value < 0.001:
        val = np.dot(np.dot(thetaT, x), -y)
        theta = theta - lr * (val*x)

    return theta

#역전파를 이용한 Affine 계층
class affine
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        y = np.dot(self.x, self.W) + self.b

        return y

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(dout, self.X.T)
        self.db =  np.sum(dout, axis=0)

class sigmoid
    def __init__(self):
        self.y = None

    def forward(self, x):
        y = 1/(1 + np.exp(-x))
        self.y = y

        return y

    def backward(self, dout):
        dx = dout * (1.0 - self.y) * self.y

        return dx

class softmax_with_loss
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t)/ batch_size

        return dx


#역전파를 이용한 gradient_desecent
