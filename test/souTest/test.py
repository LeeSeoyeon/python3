def bubbleSort(alist):
    for passnum in range(len(alist) -1, 0, -1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

def a(b):
    print(b is c)
    print(id(b))
    print(id(b[0]))

c=[5,3,2,1]
print(id(c[1]))
d = 3
c[1] = d
print(id(c[1]))
print(id(d))
print(c)