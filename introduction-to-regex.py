import re

for _ in range(int(input())):
    s = input()
    a = r'^\+*\d*\.\d*$'
    b = r'^\-*\d*\.\d*$'
    print(bool(re.match(a, s)) or bool(re.match(b, s)))
