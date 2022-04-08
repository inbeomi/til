import sys
from collections import deque

n, m = map(int, input().split())

board = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [-1, 0 , 1, 0]
dy = [0, -1, 0, 1]

count = 1

start = (0, 0, 1)
queue = deque()
queue.append(start)
# print(queue.popleft())

while queue:
    x, y, count = queue.popleft()

    if x == n and y == m:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if board[nx][ny] == '1':
                board[nx][ny] == count + 1
                queue.append((nx, ny, count+1))

print(board[n-1][m-1])