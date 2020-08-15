import numpy


n, m = tuple(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

npa = numpy.array(arr)

print(numpy.transpose(npa))
print(npa.flatten())
