#!/bin/python3

import math
import os
import random
import re
import sys


def hourglassSum(arr):
    best = -70
    for i in [0, 1, 2, 3]:
        for j in [0, 1, 2, 3]:
            count = arr[i+0][j+0] + arr[i+0][j+1] + arr[i+0][j+2] \
                                  + arr[i+1][j+1] \
                  + arr[i+2][j+0] + arr[i+2][j+1] + arr[i+2][j+2]
            if count > best:
                best = count
    return best

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
