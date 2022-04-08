# # # # 내풀이..어느 정도 방향은 잡은 거 같은데 세부사항에 대한 로직 이해가 잘 안되네 
# # # n = int(input())
# # # graph = [[input().split()] for _ in range(n)]

# # n = 5
# # graph = [['X', 'S', 'X', 'X', 'T'],
# #         ['T', 'X', 'S', 'X', 'X'],
# #         ['X', 'X', 'X', 'X', 'X'],
# #         ['X', 'T', 'X', 'X', 'X'],
# #         ['X', 'X', 'T', 'X', 'X']]

# # dp = [['X']*(n) for _ in range(n)]

# # dx = [-1, 0, 1, 0]
# # dy = [0, 1, 0, -1]

# # def watch(x, y, i):

# #     nx = x + dx[i]
# #     ny = y + dy[i]

# #     while nx >= 0 & ny >= 0 & nx < n & ny < n: 

# #         if graph[nx][ny] == 'X':
# #             graph[nx][ny] = 'T'
# #         elif graph[nx][ny] == 'S':
# #             return True
# #         else:
# #             return False
        
# #         nx = x + dx[i]
# #         ny = y + dy[i]

# #     else:
# #         return False
 
# # answer = False

# # def bfs(count):

# #     global answer

# #     if count == 3:

# #         for i in range(n):
# #             for j in range(n):
# #                 dp[i][j] == graph[i][j]

# #         for i in range(n):
# #             for j in range(n):
# #                 if dp[i][j] == 'S':
# #                     for k in range(4):
# #                         answer = watch(i, j, k)
# #         return 

# #     for i in range(n):
# #         for j in range(n):
# #             if graph[i][j] == 'X':
# #                 graph[i][j] == 'O'
# #                 count += 1
# #                 bfs(count)
# #                 graph[i][j] == 'X'
# #                 count -= 1
    
# # bfs(0)

# # if answer:
# #     print('Yes')
# # else:
# #     print('No')

# # # # # 실패함 ------------------------------------답지-------------------------------------------

# # from itertools import combinations

# # n = int(input())
# # board = []
# # teachers = []
# # spaces = []

# # for i in range(n):
# #     board.append(list(input().split()))
# #     for j in range(n):
# #         if board[i][j] == 'T':
# #             teachers.append((i,j))
# #         if board[i][j] == 'X':
# #             spaces.append((i,j))

# # def watch(x, y, direction):
# #     if direction == 0:
# #         while y >= 0:
# #             if board[x][y] == 'S':
# #                 return True
# #             if board[x][y] == 'O':
# #                 return False
# #             y -= 1

# #     if direction == 1:
# #         while y < n:
# #             if board[x][y] == 'S':
# #                 return True
# #             if board[x][y] == 'O':
# #                 return False
# #             y += 1

# #     if direction == 2:
# #         while x >= 0:
# #             if board[x][y] == 'S':
# #                 return True
# #             if board[x][y] == 'O':
# #                 return False
# #             x -= 1
    
# #     if direction == 3:
# #         while x < n:
# #             if board[x][y] == 'S':
# #                 return True
# #             if board[x][y] == 'O':
# #                 return False
# #             x += 1
    
# #     return False


# # def process():

# #     for x, y in teachers:
# #         for i in range(4):
# #             if watch(x, y, i):
# #                 return True
# #     return False

# # find = False

# # for data in combinations(spaces, 3):
# #     for x, y in data:
# #         board[x][y] = 'O'
    
# #     if not process():
# #         find = True
# #         break
    
# #     for x, y in data:
# #         board[x][y] = 'X'

# # if find:
# #     print('YES')
# # else:
# #     print('NO')

# # # # -----------------------------------------------------------------------------------------

# n = int(input())
# data = []
# teacher = []
# board = [['X' for _ in range(n)] for _ in range(n)]

# for i in range(n):
#     data.append(input().split())
#     for j in range(n):
#         if data[i][j] == 'S':
#             teacher.append((i,j))

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def view(x, y):

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 and ny >= 0 and nx < n and ny < n:
#             if board[nx][ny] == 'S':
#                 return True
#             if board[nx][ny] == 'X':
#                 board[nx][ny] = 'T'
#                 view(nx, ny)
#                 board[nx][ny] = 'X'
            
#     return False


# def wall(count):

#     if count == 3:

#         for i in range(n):
#             for j in range(n):
#                 board[i][j] = data[i][j]
        
#         for i in range(n):
#             for j in range(n):
#                 if board[i][j] == 'T':
#                     view(i, j)
#                     if view == True:
#                         break    

#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == 'X':
#                 data[i][j] = 'O'
#                 count += 1
#                 wall(count)
#                 data[i][j] = 'X'
#                 count -= 1
    
#     return 'YES'

# wall(0)

# if view == True:
#     print('YES')
# else:
#     print('No')

# # # ---------------------------------------------------------------------------------
from itertools import combinations

n = int(input())
board = []
teacher = []
empty = []
for i in range(n):
    board.append(input().split())
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append((i, j))
        elif board[i][j] == 'X':
            empty.append((i, j))

def watch(x, y, direction):
    # 왼쪽
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    # 오른쪽    
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # 위쪽
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    # 아래쪽
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x  += 1
    return False

def process():

    for x, y in teacher:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

for walls in combinations(empty, 3):

    for wall in walls:
        x, y = wall
        board[x][y] == 'O'

    # 확인
    if not process():
        find = True
        break

    for wall in walls:
        x, y = wall
        board[x][y] == 'X'

if find:
    print('YES')
else:
    print('NO')