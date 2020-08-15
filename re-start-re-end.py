import re
s, k = input(), input()
found = False
for i in range(len(s)):
    match = re.match(k,s[i:])
    if match:
        start_index = i+match.start()
        end_index = i+match.end()-1
        print((start_index,end_index))
        found = True
if found == False:
    print('(-1, -1)')
