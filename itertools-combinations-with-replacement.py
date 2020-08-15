from itertools import combinations_with_replacement

i = input().split()
s, k = sorted(i[0]), int(i[1])

for x in combinations_with_replacement(s, k):
    print(''.join(x))
