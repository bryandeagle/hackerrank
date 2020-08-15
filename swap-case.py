def swap_case(s):
    res = ''
    for c in s:
        if c.islower():
            res += c.upper()
        else:
            res += c.lower()
    return res
