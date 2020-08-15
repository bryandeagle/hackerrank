#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    numbers = dict()
    doubles = dict()
    triples = 0
    for v in arr:
        # Fill in dictionary
        if v not in numbers:
            numbers[v] = 0
        if v not in doubles:
            doubles[v] = 0
        if v/r not in numbers:
            numbers[v/r] = 0
        if v/r not in doubles:
            doubles[v/r] = 0

        # Increment total
        triples += doubles[v/r]

        # Increment doubles to record 2-tuples
        doubles[v] += numbers[v/r]

        # Increment numbers to record number
        numbers[v] += 1
    return triples

def nCr(n,r):
    f = math.factorial
    return int(f(n) / f(r) / f(n-r))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    fptr.write(str(ans) + '\n')
    fptr.close()
