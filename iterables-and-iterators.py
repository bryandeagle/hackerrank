from itertools import permutations

n = int(input())
s = input().replace(' ', '')
k = int(input())
p = [''.join(x) for x in permutations(s, k)]

num = 0
for x in p:
    if 'a' in x:
        num += 1

print(num/len(p))
