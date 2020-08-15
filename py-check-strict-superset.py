a = set(map(int, input().split()))
for _ in range(int(input())):
    ss = True
    b = set(map(int, input().split()))
    if a == b or not a.issuperset(b):
        ss = False
        break    
print(ss)
