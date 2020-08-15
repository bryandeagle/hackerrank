def merge_the_tools(string, k):
    u, i = '', 1
    for c in string:
        if c not in u:
            u += c
        if i == k:
            i = 1
            print(u)
            u = ''
        else:
            i += 1

