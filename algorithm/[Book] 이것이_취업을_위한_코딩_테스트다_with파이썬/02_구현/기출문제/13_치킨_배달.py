# n, m = map(int, input().split())
# # map_array = [[int(x) for x in input().split()] for _ in range(n)]

# n, m = (5, 2)
# map_array = [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]]

# home_array = []
# chicken_array = []

# for i in range(n):
#     for j in range(n):
#         if map_array[i][j] == 1:
#             home_array.append((i+1,j+1))
#         elif map_array[i][j] == 2:
#             chicken_array.append((i+1,j+1))

# print(home_array)
# print(chicken_array)

# result = []

# for x1, y1 in home_array:
#     box = []
#     for x0, y0 in chicken_array:
#         distance = abs(x1-x0) + abs(y1-y0)
#         box.append(distance)
#     result.append(box)

# # distance_by_chicken = []

# # for i in range(len(chicken_array)):
# #     dist = 0
# #     for j in range(len(home_array)):
# #         dist += result[j][i]
# #     distance_by_chicken.append(dist)

# # distance_by_chicken.sort()

# # print(distance_by_chicken)


# result.sort()

# print(result)

# # # 며칠 뒤... 대부분의 알고리즘을 공부한 후 다시 도전...

# from itertools import combinations
# from collections import deque

# n, m = map(int, input().split())
# chickens = []
# homes = []
# board = []

# for i in range(n):
#     board.append(list(map(int, input().split())))
#     for j in range(n):
#         if board[i][j] == 1:
#             homes.append((i, j))
#         if board[i][j] == 2:
#             chickens.append((i,j))

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# count = 0
# after_board = [[0]*n for _ in range(n)]

# def distance(x, y, chicken):

#     global count, after_board    

#     for i in range(n):
#         for j in range(n):
#             if (i, j) in homes:
#                 after_board[i][j] = 1
#             if (i, j) in chicken:
#                 after_board[i][j] = 2
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 & ny >= 0 & nx < n & ny < n:
#             if after_board[nx][ny] == 0:
#                 count += 1
#                 distance(nx, ny, chicken)
#                 count -= 1
#             else:
#                 return 

#     return count


# sum = 0
# sum_list = []
# for i in range(1, m+1):
#     pick_chicken = list(combinations(chickens, i))
#     for home in homes:
#         x, y = home
#         sum += distance(x, y, pick_chicken)
#     sum_list.append(sum)

# print(min(sum_list))

# # 일단 실패... 뭔가 구현하는 과정에서 계속 머리 속에 떠올라서 구현했는데 뭔가 부족한 듯..

# # 뭐임.. 바로 이전에 BFS가 배워서 그것을 적용시키려고 했더니만.. 더 쉽게 해버렸네.. 이래서 
# # 사람은 여러 관점에서 바라볼 줄 알아야..

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        if data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))

def get_sum(candidates):
    result = 0
    
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidates:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        
        result += temp

    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)


