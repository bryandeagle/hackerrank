n,m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
k = int(input())

data.sort(key=lambda x:x[k])

for l in data:
    print(' '.join([str(i) for i in l]))
