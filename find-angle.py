import cmath
import math

i = int(input())
r = int(input())
a = complex(r, i)
print('{:.0f}°'.format(round(math.degrees(cmath.phase(a)),0)))
