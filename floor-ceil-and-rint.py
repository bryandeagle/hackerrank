import numpy as np
np.set_printoptions(sign=' ')
array = np.array(list(input().strip().split()), dtype = float)
                 
print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))
