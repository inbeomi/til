# 맞았는지 틀렸는지 잘 모르겠다. 확실한 것은 문제에서 요구하는 기능의
# 일부를 만들지 않았다는 것. 내 생각에는 없어도 값은 나올 듯??

n, m = map(int, input().split())
a, b, d = map(int, input().split())

direction = ['북', '동', '남', '서']
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
myzip = zip(direction, steps)
mydic = dict(myzip)

map = [[int(i) for i in input().split()] for i in range(n)]

x = a
y = b

map[a][b] = 1



move = 1
turn = 0

while True:
    d -= 1
    if d == -1:
        d = 3
    # for i in range(len(direction)):
    a1, b1 = mydic[direction[d]]
    x += a1
    y += b1
    if map[x][y] == 0: 
        map[x][y] = 1
        move += 1
        turn = 0
    else:
        x -= a1
        y -= b1
        turn += 1

    if turn == 4:
        break

print(move)