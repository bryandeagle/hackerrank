k = int(input())
r = list(map(int, input().split()))
c = dict()
for x in r:
    if x not in c:
        c[x] = 1
    else:
        c[x] += 1

for l in c:
    if c[l] == 1:
        print(l)
