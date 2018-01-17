import pickle
import numpy as np

def init_network():
    with open('sample_weight.pkl', 'rb') as f:
        network = pickle.load(f)
    return network

alpha =  10 ** np.random.uniform(-8, -4)
lr = 10 ** np.random.uniform(-6, -2)

#hidden_layer 3층으로 결정하고, 각 노드의 갯수도 일단 책에 있는 내용으로 설정
hidden_layer = {'W1' : [784, 50], 'W2' : [50, 100], 'W3' : [100, 10]}
#학습률(learning rate)을 0.01
lr = 0.01
#가중치를 초기화해보자.
W1 = np.random.randn(hidden_layer['W1'][0], hidden_layer['W1'][1]) / np.sqrt(hidden_layer['W1'][0])
b1 = np.zeros(hidden_layer['W1'][1])
W2 = np.random.randn(hidden_layer['W2'][0], hidden_layer['W2'][1]) / np.sqrt(hidden_layer['W2'][0])
b2 = np.zeros(hidden_layer['W2'][1])
W3 = np.random.randn(hidden_layer['W3'][0], hidden_layer['W3'][1]) / np.sqrt(hidden_layer['W3'][0])
b3 = np.zeros(hidden_layer['W3'][1])