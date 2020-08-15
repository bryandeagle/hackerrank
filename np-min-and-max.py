import numpy as np
m,n = tuple(map(int, input().split()))
a = []
for _ in range(m):
    a.append(list(map(int, input().split())))
arr = np.array(a)
print(np.max(np.min(arr, axis=1)))
