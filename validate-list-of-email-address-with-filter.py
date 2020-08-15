import re


def fun(s):
    return re.match(r'^[A-Za-z0-9\-_]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$', s)
