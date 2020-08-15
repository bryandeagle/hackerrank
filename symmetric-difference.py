# Get input
_ = input()  # Dont care about length
M = set(map(int, input().split()))
_ = input()  # Dont care about length
N = set(map(int, input().split()))
# print('M={},N={}'.format(M,N))


a = M.union(N).difference(M.intersection(N))

for v in sorted(list(a)):
    print(v)
