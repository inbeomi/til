# # # # 내 풀이.. 실패ㅠㅠ
# # n, k = map(int, input().split())
# # array = [input().split() for _ in range(n)]
# # s, x, y = map(int, input().split())

# # dp = [[0]*n for _ in range(n)]

# # dx = [-1, 0, 1, 0]
# # dy = [0, 1, 0, -1]

# # def spread(array, x, y):
# #     k = array[x][y]

# #     for i in range(4):
# #         nx = x + dx
# #         ny = y + dy

# #         if nx >= 0 and ny >= 0 and nx < n and ny < n:
# #             if array[nx][ny] == 0:
# #                 array[nx][ny] = k

# # time = 0
# # while s-time:
# #     for i in range(1, k+1):
# #         for j in range(n):
# #             for k in range(n):
# #                 if array[j][k] == i:
# #                     spread(array, j, k)

# #     time += 1

# # print(array)
# # print(array[x-1][y-1])

# # # # ----------------------답지 봄--------------------------------

# from collections import deque

# n, k = map(int, input().split())

# graph = []
# data = []

# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     for j in range(n):
#         if graph[i][j] != 0:
#             data.append((graph[i][j], 0, i, j))

# data.sort()
# q = deque(data)

# target_s, target_x, target_y = map(int, input().split())

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# while q:
#     virus, s, x, y = q.popleft()

#     if s == target_s:
#         break
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 and ny >=0 and nx < n and ny < n:
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = virus
#                 q.append((virus, s+1, nx, ny))

# print(graph[target_x -1][target_y -1])

# # # -----------------------------------------------------------------------------------------------
from collections import deque

n, k = map(int, input().split())

data = []
virus = []

for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j], 0, i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

target_s, target_x, target_y = map(int, input().split())

virus.sort()
queue = deque(virus)

while queue:
    name, s, x, y = queue.popleft()

    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = name
                queue.append((data[nx][ny], s+1, nx, ny))
    
print(data[target_x-1][target_y-1])
        

