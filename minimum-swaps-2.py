#!/bin/python3

import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    counter = 0
    temp = [0] * len(arr)

    for index, value in enumerate(arr):
        temp[value-1] = index

    for i in range(len(arr)):
        if arr[i] != i+1:
            t = temp[i]
            arr[i], arr[t] = i+1, arr[i]
            temp[i], temp[arr[t]-1] = i, t
            counter += 1
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
