def ping(n):
    if(n%2==0):
        return True
    else:
        return False

def printing(num):

    val = ping()
    if(val==True):
        print("Number is even")
    else:
         print("Number is odd")
         number = int(input())
         printing(number)
# method 1
import math
print(math.pi)
#method 2
from math import *
print(pi)
#method 3
'''
from math import pi
print(pi)'''
print(factorial(6))
print(ceil(7.8))
print(floor(7.8))
print(gcd(34,85))