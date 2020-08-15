h, w = [int(i) for i in input().split(' ')]


for n in range(h//2):
    print(('.|.'*(2*n+1)).center(w,'-'))

print('WELCOME'.center(w,'-'))

for n in reversed(range(h//2)):
    print(('.|.'*(2*n+1)).center(w,'-'))
