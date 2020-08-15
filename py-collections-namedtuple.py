from collections import namedtuple
n, Student = int(input()), namedtuple('Student',','.join(input().split()))
students = [Student(*input().split()) for _ in range(n)]
print(sum([int(s.MARKS) for s in students])/n)
