import numpy as np
a = np.array([list(map(float, input().split())) for _ in range(int(input()))])
print(np.round(np.linalg.det(a), 2))
