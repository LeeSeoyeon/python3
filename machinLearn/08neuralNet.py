import numpy as np

class NeuralNet:
    network = {}
    def __init__(self):
        network = {}
        network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
        network['b1'] = np.array([0.1, 0.2, 0.3])
        network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
        network['b2'] = np.array([0.1, 0.2])
        network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
        network['b3'] = np.array([0.1, 0.2])

        self.network = network

    def sigmoid(self,x):
        return 1/(1 + np.exp(-x))

    def identityFun(self, x):
        return x

    def forword(self, x):

        network = self.network
        W1, W2, W3 = network['W1'], network['W2'], network['W3']
        b1, b2, b3 = network['b1'], network['b2'], network['b3']

        A1 = np.dot(x, W1) + b1
        Z1 = self.sigmoid(A1)
        print(Z1)
        A2 = np.dot(Z1, W2) + b2
        Z2 = self.sigmoid(A2)

        A3 = np.dot(Z2, W3) + b3
        y = self.identityFun(A3)

        return y

x = np.array([1.0, 0.5])
y = NeuralNet().forword(x)

print("input Value = {} , result = {}".format(x, y))



