#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    res = list()
    cnt = dict()
    frq = dict()

    for c,x in queries:
        if c == 1:
            if x not in cnt:
                cnt[x] = 0
            if cnt[x] > 0:
                frq[cnt[x]] -= 1
            cnt[x] += 1  # Add number
            if cnt[x] in frq:
                frq[cnt[x]] += 1
            else:
                frq[cnt[x]] = 1
            #print('({},{}) cnt={} frq={}'.format(c,x,cnt,frq))
            
        elif c == 2:
            if x in cnt and cnt[x] > 0:
                frq[cnt[x]] -= 1
                cnt[x] -= 1  # Remove if present
                if cnt[x] in frq and cnt[x] > 0:
                    frq[cnt[x]] += 1
                elif cnt[x] > 0:
                    frq[cnt[x]] = 1
                #print('({},{}) cnt={} frq={}'.format(c,x,cnt,frq))

        elif c == 3:
            if x in frq and frq[x] > 0:
                #print('({},{}) cnt={} frq={} res=Yes'.format(c,x,cnt,frq))
                res.append(1)
            else:
                #print('({},{}) cnt={} frq={} res=No'.format(c,x,cnt,frq))
                res.append(0)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = freqQuery(queries)
    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')
    fptr.close()
