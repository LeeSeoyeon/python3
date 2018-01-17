import numpy as np

def calXYZ(cLen):
    maxValue, maxX, maxY = 0.0 , 0.0 , 0.0

    for a in np.arange(0, cLen + 0.1, 0.1):
        temp = 0.0
        b = cLen - a

        x = np.sqrt(a**2 + b**2)
        y = np.sqrt((cLen-a)**2 + b**2)
        z = np.sqrt(a**2 + (cLen-b)**2)

        temp = x + y + z
        print(temp)
        if temp > maxValue:
            maxValue = temp
            maxX = a
            maxY = b

    return [maxValue, maxX, maxY]

def calAB(cLen, a, b):
    x = np.sqrt(a ** 2 + b ** 2)
    y = np.sqrt((cLen - a) ** 2 + b ** 2)
    z = np.sqrt(a ** 2 + (cLen - b) ** 2)

    return x + y + z

cLen = 2.0
print(np.sqrt(2))

test =  calXYZ(cLen)
a = 4/(2+np.sqrt(2))
print("prediect maxValue : {} or  {}".format(calAB(cLen, a, a), np.sqrt(2)*2*(3/2)))
print("real maxVale : {}".format(test))

