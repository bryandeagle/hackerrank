import numpy as np
np.set_printoptions(sign=' ')
m,n = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(m)]
print(np.mean(a, axis=1), np.var(a, axis=0), np.std(a).round(decimals=12), sep='\n')
