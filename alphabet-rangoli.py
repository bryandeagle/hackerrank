def print_rangoli(size):
    w = 4 * size - 3
    for i in range(size-1, -1, -1):
        arr = [x for x in range(size, i, -1)]
        chrs = [chr(96+x) for x in arr[:-1] + arr[::-1]]
        print('-'.join(chrs).center(w, '-'))
    for i in range(1, size):
        arr = [x for x in range(size, i, -1)]
        chrs = [chr(96+x) for x in arr[:-1] + arr[::-1]]
        print('-'.join(chrs).center(w, '-'))
