import numpy as np
m, n, p = tuple(map(int, input().split()))
a, b = [], []
for _ in range(m):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))

na = np.array(a)
nb = np.array(b)

print(np.concatenate((na, nb)))
