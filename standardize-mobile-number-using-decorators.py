def fix(num):
    if len(num) == 10:
        return '+91 ' + num[0:5] + ' ' + num[5:10]
    elif len(num) == 11:
        return '+91 ' + num[1:6] + ' ' + num[6:11]
    elif len(num) == 12:
        return '+91 ' + num[2:7] + ' ' + num[7:12]
    elif len(num) == 13:
        return '+91 ' + num[3:8] + ' ' + num[8:13]
    else:
        return num

def wrapper(f):
    def fun(l):
        return f([fix(k) for k in l])
    return fun
