n = int(input())
plan = input().split()

x = 1
y = 1

L = (0, -1)
R = (0, 1)
U = (-1, 0)
D = (1, 0)

move = dict(L= L,
            R= R,
            U= U,
            D= D)

for i in range(len(plan)):

    x += move[plan[i]][0]
    y += move[plan[i]][1]
    if 1 <= x <= n and 1 <= y <= n:
        continue
    else:
        x -= move[plan[i]][0]
        y -= move[plan[i]][1]

print(x, y)
