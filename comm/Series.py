def arithmeticSeries(a, n):
    return (a + n*a)*n//2


def getFibonacci(init1=1, init2=2, length=2):
    arr = []
    arr[0] = init1
    arr[1] = init2

    for i in range(2, length):
        arr[i] = arr[i-1] + arr[i-2]

    return arr