from collections import defaultdict

(n, m) = map(int, input().split(' '))
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    w = input()
    if len(d[w]) == 0:
        print(-1)
    else:
        print(' '.join(map(str, d[w])))
