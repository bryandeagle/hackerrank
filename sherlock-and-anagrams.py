#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    d = dict()
    for n in range(len(s)-1):
        ana = [''.join(sorted(s[i:i+n+1])) for i in range(len(s)-n)]
        for a in ana:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
    return sum([int((d[x]*(d[x]-1))/2) for x in d])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()
