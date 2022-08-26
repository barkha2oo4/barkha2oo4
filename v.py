

# MAX AND MIN SUM OF 4 ELEMENTS OF AN ARRAY
'''
def miniMaxSum(arr):
    arr.sort()
    miniSum = 0
    maxSum = 0 
    for i in range(4):
     miniSum += arr[i]
        
    print(miniSum, end="  ")
        
    for i in range(4,0,-1):
        maxSum += arr[i]
        
    print(maxSum, end="  ")
       
    
if __name__ == '__main__':

    arr =list(map(int,input().rstrip().split()))
    miniMaxSum(arr)'''

   
    #BIRTHDAY CAKE CANDLES
import os


def birthdayCakeCandles(ar):
    k =max(ar)
    count = 0
    for i in ar:
        if i == k:
            count +=1
    return count
if __name__ == '__main__':

    #birthday cake method 2

 def birthdayCakeCandles(ar):
    ar.sort()
    result = ar.count(ar[len(ar)-1])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()









