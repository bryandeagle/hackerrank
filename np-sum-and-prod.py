import numpy as np
m,n = tuple(map(int, input().split()))
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

arr = np.array(a)
print(np.prod(np.sum(arr, axis=0)))
