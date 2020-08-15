(m,n) = map(int, input().split())
g = [list(map(float, input().split())) for _ in range(n)]
for h in list(zip(*g)):
    print(sum(h)/n)
