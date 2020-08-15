cube = lambda x: x**3

def fibonacci(n):
    f = [0, 1, 1]
    if n <= 3:
        return f[:n]
    else:
        for i in range(n-3):
            f.append(f[-1]+f[-2])
    return f
