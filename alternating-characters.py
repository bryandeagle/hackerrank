#!/bin/python3

import math
import os
import random
import re
import sys


def alternatingCharacters(s):
    dels, prev = 0, None
    for c in s:
        if c == prev:
            dels += 1
        else:
            prev = c
    return dels

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()
