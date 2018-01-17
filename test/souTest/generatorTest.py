import os
import sys

def aafor():
    for i in range(10000):
        showaa()

aa = aafor;
def showaa():
    global aa
    print(sys.getsizeof(aa))

if __name__ == "__main__":
   aa()

   print(sys.getsizeof(i for i in range(10000)))