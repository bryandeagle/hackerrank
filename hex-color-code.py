import re
s = ''
for _ in range(int(input())):
    s += input().replace('\s', '')

for p in re.findall(r'\{.*?\}', s):
    for m in re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}', p):
        print(m)
