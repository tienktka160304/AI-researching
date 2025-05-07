# a = [1, 2, 3]
# b = [3, 2, 1]

# For elements *0*, Bob is awarded a point because a[0] < b[0].
# For the equal elements a[1] and b[1], no points are earned.
# Finally, for elements 2, a[2] > b[2] so Alice receives a point.
# The return array is [1, 1] with Alice's score first and Bob's second.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    x = 0
    y = 0
    for i in range(3):
        if a[i] > b[i]:
            x += 1
        elif a[i] < b[i]:
            y += 1
    return x, y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
