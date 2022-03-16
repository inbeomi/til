word = input()

# 97(a) - 122(z)
count = [0]*26

for i in word:
    count[ord(i)-97] += 1

print(' '.join([str(count[i]) for i in range(len(count))]))

