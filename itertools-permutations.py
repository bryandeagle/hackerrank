from itertools import permutations

i = input().split()
s, k = sorted(i[0]), int(i[1])
for x in permutations(s, k):
    print(''.join(x))
