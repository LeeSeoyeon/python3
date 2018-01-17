import numpy as np

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    print(x[0])
    print(x.size)
    for idx in range(x.size):
        tmp_val = x[idx]

        tmp_val = tmp_val + h
        fxh1 = f(tmp_val)

        tmp_val = tmp_val - h
        fxh2 = f(tmp_val)

        grad[idx] = ((fxh1 - fxh2) / (2*h))

    return grad

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f,x)
        print(grad)
        x -= lr * grad

    return x

def function_2(x):
    return x[0]**2 + x[1]**2

result = gradient_descent(function_2, np.array([[-3.0, 4.0],[3.0, 4.0], [3.0, -4.0]]), 0.01, 100)

print(result)