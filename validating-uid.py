import re

for _ in range(int(input())):
    x = input()

    if len(x) != 10:
        print('Invalid')
    elif not re.match(r'^\w*$', x):
        print('Invalid')
    elif len(re.findall(r'[A-Z]', x)) < 2:
        print('Invalid')
    elif len(re.findall(r'\d', x)) < 3:
        print('Invalid')
    elif re.search(r'(.).*\1', x):
        print('Invalid')
    else:
        print('Valid')
