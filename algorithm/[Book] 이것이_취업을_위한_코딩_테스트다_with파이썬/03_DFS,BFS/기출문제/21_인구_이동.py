# n, L, R = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# dp = [[0]*n for _ in range(n)]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def bfs(x, y):

#     for i in range(n):
#         for j in range(n):
#             if 

# # # ㅠㅠ -------------------------------------------------------------------

# 일단 연합국가가 어떻게 되는지를 나타내야 하고.
# 그리고 며칠동안 인구이동이 나타났는지

from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def process(x, y, index):

    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    union[x][y] = index
    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    # 하루를 기준으로 연합인 국가를 확인해보는 것이구만.. 그래서 하루가 지나면 다시 서로 다른 국가로..
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1

    if index == n * n :
        break
    total_count += 1

print(union)
print(total_count)


