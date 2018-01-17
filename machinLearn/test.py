import numpy as np
import matplotlib.pyplot as plt

dataSet2 = ([1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11],[12,12],[13,13],[14,14],[15,15],[16,16],[17,17],[18,18],[19,19],[20,20])
dataSet3 = ([1,3],[2,5],[3,7],[4,9],[5,11],[6,13],[7,15],[8,17],[9,19],[10,21],[11,23],[12,25],[13,27],[14,29],[15,31],[16,33],[17,35],[18,37],[19,39],[20,41])

lr = 0.01
M = len(dataSet3)
print("데이터크기 M = {}".format(M))
print("learning rate Alpha = {}".format(lr))

#DataSet을 그래프의 각 x,y로 표시해주기 위해서 1차 배열로 바꾸어준다.
x = []
y = []
for row in dataSet3:
    x.append(row[0])
    y.append(row[1])

class heightAndWeight:
    def showDataSet(self, theta0, theta1):

        plt.plot(x, y, 'rs')
        plt.xlabel('X')
        plt.ylabel('Y')

        x2 = np.arange(1, M)
        y2 = theta0 + theta1*x2

        plt.plot(x2, y2)

        plt.show()

    def costFunction(self, theta0, theta1):
        #theta0  , theta1 = np.arange(-1, 1, 0.1), np.arange(-1, 1, 0.1)

        #데이타 셋에 대한 세타0, 세타1에 대한 소비함수를 그려보자
        costSum  = [];
        for j in np.arange(0, M):
            sum = 0
            for i in np.arange(0,M):
                sum += (theta0[j] + 4/9*x[i] - y[i]) **2
            costSum.append(sum/(2*M))

        plt.plot(theta0, costSum, 'rs')
        plt.xlabel("theta")
        plt.ylabel("Cost Function")
        plt.show()

    def gradient_descent(self, theta0 =3, theta1 =4, count=100):
        #초기 theta값을 인자로 설정
        thetaX0, thetaX1 = [], []
        for j in np.arange(0,count):
            #기울기
            grad0 , grad1 = 0, 0
            ySum = 0
            xSum = 0
            for i in np.arange(0,M):
                grad0 += theta0 + theta1*x[i] - y[i]
                grad1 += (theta0 + theta1*x[i] - y[i])*x[i]

            grad0 = lr*grad0/M
            grad1 = lr*grad1/M

            theta0 = theta0 - grad0
            thetaX0.append(theta0)
            theta1 = theta1 - grad1
            thetaX1.append(theta1)

            print("{}번째 : theta0 = {}, theta1 = {}".format(j, theta0, theta1))

        #self.costFunction(thetaX0, thetaX1)

        return [theta0, theta1, thetaX0, thetaX1]




test = heightAndWeight()
#test.showDataSet()
#test.costFunction(np.arange(-9, -8, 0.05), np.arange(-1, 1, 0.1))
test.showDataSet(1,1)
testTheta = test.gradient_descent(1,1, 100)
test.showDataSet(testTheta[0], testTheta[1])
