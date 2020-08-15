from collections import Counter

_ = input()
shoes = Counter(map(int, input().split(' ')))
revenue = 0
for _ in range(int(input())):
    (size, cost) = map(int, input().split(' '))
    if shoes[size] > 0:
        revenue += cost
        shoes[size] -= 1
print(revenue)
