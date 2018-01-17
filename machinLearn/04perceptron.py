#AND, NAND, OR 게이트를 구현
from builtins import print


class Perceptron:
    def AND(self, x1, x2):
        w1, w2, theta = 0.5, 0.5, 0.7
        tmp = x1*w1 + x2*w2
        if tmp <= theta:
            return 0
        elif tmp > theta:
            return 1

    def NAND(self, x1, x2):
        w1, w2, theta = -0.5, -0.5, -0.7
        tmp = x1 * w1 + x2 * w2
        if tmp >= theta:
            return 1
        elif tmp < theta:
            return 0

    def OR(self, x1, x2):
        w1, w2, theta = 0.5, 0.5, 0.3
        tmp = x1 * w1 + x2 * w2
        if tmp <= theta:
            return 0
        elif tmp > theta:
            return 1


test = Perceptron()
print("AND Test -----------------------")
print("x1 = {}, x2 = {}, AND = {}".format(0, 0, test.AND(0,0)))
print("x1 = {}, x2 = {}, AND = {}".format(1, 0, test.AND(1,0)))
print("x1 = {}, x2 = {}, AND = {}".format(0, 1, test.AND(0,1)))
print("x1 = {}, x2 = {}, AND = {}".format(1, 1, test.AND(1,1)))

print("NAND Test -----------------------")
print("x1 = {}, x2 = {}, NAND = {}".format(0, 0, test.NAND(0,0)))
print("x1 = {}, x2 = {}, NAND = {}".format(1, 0, test.NAND(1,0)))
print("x1 = {}, x2 = {}, NAND = {}".format(0, 1, test.NAND(0,1)))
print("x1 = {}, x2 = {}, NAND = {}".format(1, 1, test.NAND(1,1)))

print("OR Test -----------------------")
print("x1 = {}, x2 = {}, OR = {}".format(0, 0, test.OR(0,0)))
print("x1 = {}, x2 = {}, OR = {}".format(1, 0, test.OR(1,0)))
print("x1 = {}, x2 = {}, OR = {}".format(0, 1, test.OR(0,1)))
print("x1 = {}, x2 = {}, OR = {}".format(1, 1, test.OR(1,1)))


import numpy as np

class PerceptronNumpy():

    def AND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.7

        if np.sum(w*x)+b <= 0:
            return 0
        else:
            return 1

    def NAND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([-0.5, -0.5])
        b = 0.7

        if np.sum(w*x)+b >= 0:
            return 1
        else:
            return 0

    def OR(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.3

        if np.sum(w*x)+b <= 0:
            return 0
        else:
            return 1

    def XOR(self, x1, x2):
        s1 = self.NAND(x1, x2)
        s2 = self.OR(x1, x2)

        print("s1 = {}, s2 = {}".format(s1, s2))

        return self.AND(s1,s2)


#다층 퍼셉트론으로 표현한 XOR => 단일 퍼셉트론으로 XOR을 구현할수 없다.
test2 = PerceptronNumpy()
print("XOR Test by Numpy -----------------------")
print("x1 = {}, x2 = {}, XOR = {}".format(0, 0, test2.XOR(0,0)))
print("x1 = {}, x2 = {}, XOR = {}".format(1, 0, test2.XOR(1,0)))
print("x1 = {}, x2 = {}, XOR = {}".format(0, 1, test2.XOR(0,1)))
print("x1 = {}, x2 = {}, XOR = {}".format(1, 1, test2.XOR(1,1)))


