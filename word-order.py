from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    line = input()
    if line in d:
        d[line] += 1
    else:
        d[line] = 1
print(len(d))
print(' '.join([str(d[i]) for i in d.keys()]))
