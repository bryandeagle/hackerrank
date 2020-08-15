def p(num):
    return str(num) == str(num)[::-1]

_ = input()

arr = list(map(int, input().split()))
pos = all([x > 0 for x in arr])
pal = any([p(x) for x in arr])
print(pos and pal)
