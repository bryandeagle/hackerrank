#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    deletions = 0
    fa = [0] * 26
    fb = [0] * 26

    for c in a:
        fa[ord(c)-97] += 1
    
    for c in b:
        fb[ord(c)-97] += 1

    difference = [abs(fa[i]-fb[i]) for i in range(26)]
    return sum(difference)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
