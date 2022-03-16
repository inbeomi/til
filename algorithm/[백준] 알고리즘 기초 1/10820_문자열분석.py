import sys
sentence = sys.stdin.readline()

lower = 0
upper = 0
num = 0
space = 0

for i in sentence:
    if ord(i) >= 65 and ord(i) < 91:
        upper += 1
    elif ord(i) >= 97 and ord(i) < 123:
        lower += 1
    elif i.isdigit():
        num += 1
    else:
        space += 1

print(lower, upper, num, space)


