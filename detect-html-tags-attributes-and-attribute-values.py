import re

s = ''
for _ in range(int(input())):
    s += input()

s = re.sub(r'<\!--.*?-->', '', s)
s = re.sub(r'\s+', ' ', s)

for m in re.findall(r'<(\w.*?)/?>', s):
    t = re.split(r' +', m, 1)
    print(t[0])
    if len(t) > 1:
        for x in re.finditer(r'(\S*?)=[\'\"](.*?)[\'\"]', t[1]):
            print('-> {} > {}'.format(x.group(1), x.group(2)))
