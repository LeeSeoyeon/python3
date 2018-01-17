#GCM
def getGCM(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    return getGCM(b, a%b)

#LCM
def getLCM(a, b):
    return a * b // getGCM(a, b)
