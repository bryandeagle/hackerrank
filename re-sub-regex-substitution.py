import re
for _ in range(int(input())):
    s = re.sub(r'(?<=\s)\&\&(?=\s)', 'and', input())
    s = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', s)
    print(s)
