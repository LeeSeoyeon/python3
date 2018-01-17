import numpy as np

def stepFunction(x):
    if x>0:
        return 1
    else:
        return 0

result = stepFunction(1.0)
print(result)
result = stepFunction(2.0)
print(result)
result = stepFunction(3.0)
print(result)

#배열도 받는 stpeFunction
def stepFunctionArr(x):
    y =  x>0
    return y.astype(np.int)


result = stepFunctionArr(np.array([-1.0, 1.0, 2.0]))
print(result)

#계단함수 그래프로 표현
import matplotlib.pylab as plt

def stepFunctionGraph(x):
    return np.array(x>0, dtype=np.int)
x = np.arange(-0.5, 5.0, 0.1)
y = stepFunctionGraph(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.show()