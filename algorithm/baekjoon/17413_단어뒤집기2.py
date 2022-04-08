# %%
import sys
s = list(sys.stdin.readline().rstrip())

i = 0
check = 0

while i < len(s):
    if s[i] == "<":
        i += 1
        while s[i] != ">":
            i += 1
        i += 1
    elif s[i].isalnum():
        check = i
        while i < len(s) and s[i].isalnum():
            i += 1
        temp = s[check:i]
        temp.reverse()
        s[check:i] = temp
        # s[check:i] = s[check:i].reverse()
    else:
        i += 1

print(''.join(s))


# %%
