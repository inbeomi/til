# n, m = map(int, input().split())

# # # 와 진짜 BPS, DPS는 어떻게 접근해야 할지 감이 안 잡히네
# # # 답지를 볼 때, 설마 했던 방식으로 접근하는 것을 보고.. 흑,,
# data = []
# temp = [[0]*m for _ in range(n)]

# for _ in range(n):
#     data.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# result = 0

# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)

# def get_score():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score



# def dfs(count):
#     global result

#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = data[i][j]

#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)

#         result = max(result, get_score())
#         return

#     # 울타리를 이렇게 심어가네.. 미친..
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1

# print(dfs(0))
# print(result)


n, m = map(int, input().split())
data = [[x for x in map(int, input().split())] for _ in range(n)]
temp = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

result = 0

def dfs(count):

    global result

    if count == 3:
        
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return 
        


    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)
