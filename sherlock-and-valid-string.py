#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    freqs = {}
    for c in s:
        if c not in freqs:
            freqs[c] = 1
        else:
            freqs[c] += 1

    freq_list = [freqs[k] for k in freqs]
    max_val = max(freq_list)
    min_val = min(freq_list)
    max_cnt = freq_list.count(max_val)
    min_cnt = freq_list.count(min_val)
    
    print('F={},MNV={},MXV={},MNC={},MXC={}'
        .format(freqs, min_val, max_val, min_cnt, max_cnt))

    if min_val == max_val:
        return 'YES'
    elif max_val == (min_val + 1) and max_cnt == 1:
        return 'YES'
    elif min_cnt == 1 and min_val == 1 and min_cnt + max_cnt == len(freq_list):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()
