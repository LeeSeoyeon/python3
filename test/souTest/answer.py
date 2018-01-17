n = int(input())
n5 = next((i for i in reversed(range(int(n/5))) if (n - 5*i)%3 is 0 ))
print(n5)
#print(int(n5 + (n - 5*n5)/3))
