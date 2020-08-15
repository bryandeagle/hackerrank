from itertools import combinations

i = input().split()
s, m = sorted(i[0]), int(i[1])

for k in range(1,m+1):
    for x in list(combinations(s, k)):
        print(''.join(x))
