import itertools

(K, N) = map(int, input().strip().split())

L = list()
for i in range(K):
    L.append(list(map(int, input().strip().split(' ')))[1:])

S_max, L_max = 0, None
for l in itertools.product(*L):
    s = sum([x**2 for x in l]) % N

    if s > S_max:
        S_max = s
        L_max = l

print(S_max)
