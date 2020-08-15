for _ in range(int(input())):
    try:
        (a, b) = map(int, input().split())
        print(a//b)
    except (ValueError, ZeroDivisionError) as e:
        print('Error Code: {}'.format(e))
