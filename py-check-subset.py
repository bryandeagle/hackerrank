for _ in range(int(input())):
    _ = input()
    a = set(map(int, input().split()))
    _ = input()
    b = set(map(int, input().split()))
    if a.issubset(b):
        print(True)
    else:
        print(False)
