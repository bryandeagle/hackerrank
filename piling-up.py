from collections import deque

for _ in range(int(input())):
    _ = input()
    h = deque(map(int, input().split()))
    
    res, v = '', 2**31
    l, r = h.popleft(), h.pop()
    while res == '':
        # print('v={},l={},r={},h={}'.format(v,l,r,list(h)))
        if l >= r and l <= v:
            v = l
            if len(h) == 0:
                res = 'Yes'
                break
            l = h.popleft()
        elif r > l and r <= v:
            v = r
            if len(h) == 0:
                res = 'Yes'
                break
            r = h.pop()
        else:
            res = 'No'
    print(res)
