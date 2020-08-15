from itertools import groupby

print(' '.join(['({}, {})'.format(len(list(g)), k) for k,g in groupby(input())]))
