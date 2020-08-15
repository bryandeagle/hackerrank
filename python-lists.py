if __name__ == '__main__':
    arr = []
    N = int(input())
    for _ in range(N):
        line = input().split(' ')
        
        # Parse the command
        cmd = line[0]
        if len(line) > 1:
            x = int(line[1])
        if len(line) > 2:
            y = int(line[2])
        if cmd == 'insert':
            arr.insert(x, y)
        elif cmd == 'print':
            print(arr)
        elif cmd == 'remove':
            arr.pop(arr.index(x))
        elif cmd == 'append':
            arr.append(x)
        elif cmd == 'sort':
            arr = sorted(arr)
        elif cmd == 'pop':
            arr.pop()
        elif cmd == 'reverse':
            arr.reverse()
