import re

r = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

results = re.findall(r,input())
if not results:
    print(-1)
else:
    for x in results:
        print(x)
