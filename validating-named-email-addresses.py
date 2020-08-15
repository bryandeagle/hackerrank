import re
for _ in range(int(input())):
    name, email = input().split()
    if re.match(r'^<[A-Za-z][\w\-\.\_]*@[A-Za-z]+\.[A-Za-z]{1,3}>$', email):
        print('{} {}'.format(name, email))
