
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    l = len(arr)
    neg = 0
    zero = 0
    pos = 0
    for i in range(l):
        if arr[i] < 0 :
            neg += 1
        elif arr[i] == 0:
            zero += 1
        else: 
            pos += 1
    print(pos/l)
    print(neg/l)
    print(zero/l)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
