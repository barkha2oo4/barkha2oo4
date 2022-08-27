
''' randint means random integers
randit (2,100)
2
98
79
80
5
5
'''
# method1
import random
from random import randint
k = random.randint(2,100)
print(k)

avengers = ["hulk","iron man", "Captain America","spiderman","black panther","black widow","doctor strange","thor","ant man"]
l = len(avengers)
k = randint(0,l-1)
#  print(avengers[k])
# to print the number of dashes same as no. of characters

s =""
for i in avengers[k]:
    if(i==' ' or i=="a"or i=="o" or i=='i'or i =='u'or i=="e"):
        s += i
        s +=" "     
        continue
    s+="_"
print(s)
   
