import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x+y)

#Broadcast
print(x/2.0)

A = np.array([[1,2], [3,4], [5,6]])
print(A)

print(A.shape)
print(A.dtype)

grad = [1.01, 1.02]
print( grad * 0.01)