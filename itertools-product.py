from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(' '.join(list([str(x) for x in product(a, b)])))
