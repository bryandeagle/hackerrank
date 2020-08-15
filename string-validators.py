if __name__ == '__main__':
    s = input()
    alnum, alpha, digit, lower, upper = False, False, False, False, False
    for t in s:
        alnum |= t.isalnum()
        alpha |= t.isalpha()
        digit |= t.isdigit()
        lower |= t.islower()
        upper |= t.isupper()
    print('{}\n{}\n{}\n{}\n{}'.format(alnum, alpha, digit, lower, upper))
