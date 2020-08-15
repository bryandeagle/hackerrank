# Get the input values
_ = input()  # Don't care about 1st line
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

score = 0
for n in arr:
    if n in a:
        score += 1
    elif n in b:
        score -=1
print(score)
