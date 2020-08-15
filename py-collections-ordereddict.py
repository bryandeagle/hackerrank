from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    line = input().split()
    product = ' '.join(line[:-1])
    price = int(line[-1])
    if product not in d:
        d[product] = price
    else:
        d[product] += price

for x in d:
    print('{} {}'.format(x, d[x]))
