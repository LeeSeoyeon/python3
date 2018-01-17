def getPrimeList(num):
    primeList = []
    for i in range(2, num + 1):
        check = True
        for j in primeList:
            if j > num**0.5:
                break

            if i%j is 0 :
                check = False
                break


        if check :
            primeList.append(i)

    return primeList

def getPrimeListWithCount(num):
    primeList = []
    i =1
    while(len(primeList) != num):
        i += 1
        check = True
        for j in primeList:

            if i%j is 0 :
                check = False
                break

            if j > i**0.5:
                break

        if check :
            primeList.append(i)

    return primeList