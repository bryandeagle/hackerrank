_ = input()
a = set(map(int, input().split()))
for _ in range(int(input())):
    op = input().split()[0]
    s = set(map(int, input().split()))
    if op == 'intersection_update':
        a.intersection_update(s)
    elif op == 'difference_update':
        a.difference_update(s)
    elif op == 'symmetric_difference_update':
        a.symmetric_difference_update(s)
    elif op == 'update':
        a.update(s)
print(sum(a))
