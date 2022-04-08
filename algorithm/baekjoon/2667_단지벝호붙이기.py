n = int(input())
n = 7

map = [[] for _ in range(n)]

print(map)

from collections import deque

n = int(input())
print(n)

check = [[0 for _ in range(n)] for _ in range(n)]
print(check)

# map = []

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# for i in range(n):
#     map.append(list(input()))
    
# def bfs(x,y):

    

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 and ny >= 0 and nx < n and ny < n:
#             if map[nx][ny] == 1:
#               pass