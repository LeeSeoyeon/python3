import numpy as np

#훈련과 시험할 데이터를 가져온다.
import loadData

(x_train, t_train), (x_test, t_test) = loadData.load_mnist(False, True, True)

#가중치 받아오기
import net_weight

network = net_weight.init_network()

#활성화 함수를 로드
from hypothesis_function import sigmoid
from hypothesis_function import softmax

a1 = np.dot(x_test[0] , network['W1']) + network['b1']
print("1")
z1 = sigmoid(a1)
print(z1)
a2 = np.dot(z1 , network['W2']) + network['b2']
print("2")
z2 = sigmoid(a2)
a3 = np.dot(z2 , network['W3']) + network['b3']
y = softmax(a3)

#list에서 가장 큰 값의 index 찾기
def max_value_find(list):
    max = np.max(list)
    return [i for i, x in enumerate(list) if x == max]

print('---------------------------')
print("test value : {}, label : {} ".format(max_value_find(y), max_value_find(t_test[0])))


def accuracy(y, t):
    accuracy_cnt = 0
    for i in y:
        p = np.argmax(y[i])
        if p == t[i]:
            accuracy_cnt += 1

    return accuracy_cnt

