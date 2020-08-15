from collections import deque
d = deque()
for _ in range(int(input())):
    line = input().split()
    if line[0] == 'append':
        d.append(int(line[1]))
    elif line[0] == 'appendleft':
        d.appendleft(int(line[1]))
    elif line[0] == 'pop':
        d.pop()
    elif line[0] == 'popleft':
        d.popleft()
print(' '.join(map(str, d)))
