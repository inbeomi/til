n = input()

left = []
right = []

for i in range(len(n)):
    if i < (len(n)/2):
        left.append(int(n[i]))
    else:
        right.append(int(n[i]))

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")