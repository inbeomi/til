# 1시간 30분.. 실패..

# # 보드의 크기와 사과의 개수
# n = int(input())
# k = int(input())

# # 사과의 좌표를 x, y로 나눠서 설정
# apple_x = []
# apple_y = []

# # 입력 받을 시간초와 방향 공간 설정
# time_list = []
# direct_list = []

# # 뱀의 방향 움직임 설정. 
# move_list = [(1,0), (0,1), (-1,0), (0,-1)]
# left_list = [(0,1), (-1,0), (0,-1), (1,0)]
# right_list = [(0,-1), (1,0), (0,1), (-1,0)]

# # 사과의 위치를 사과의 개수만큼 입력받음
# for _ in range(k):
#     row, column = map(int, input().split())
#     apple_x.append(row)
#     apple_y.append(column)

# # 뱀이 몇 번 방향을 틀 것인지 입력을 받음
# l = int(input())

# # 방향을 틀을 횟수만큼 방향을 틀을 시간초와 방향을 입력 받아 저장함
# for _ in range(l):
#     time, direct = input().split()
#     time_list.append(int(time))
#     direct_list.append(direct)

# # 방향을 바꾸는 함수 설정
# def turn(move ,direct):
#     if direct == "L":
#         i = move_list.index(move)
#         return left_list[i]
#     else:
#         i = move_list.index(move)
#         return right_list[i]

# # 뱀의 위치 설정
# snake_x = [1]
# snake_y = [1]

# # 시간 
# count = 0

# #뱀의 첫 방향
# move = (0,1)

# i = 0
# j = 0
# k = 0

# # print(time_list)
# # print(direct_list)
# print(apple_x)
# # print(apple_y)

# while True:

   
    
#     # 현재 위치를 저장하느 변수 설정
#     prev_x = snake_x[-1]
#     prev_y = snake_y[-1]

#     # 뱀 움직이기. 
#     for z in range(k+1):
#         snake_x[z] += move[0]
#         snake_y[z] += move[1]
    
#     print('움직임', snake_x, snake_y)
#     # 움직였으니 1초 
#     count += 1
    
#     print(count, '초', sep='')

#     if count == time_list[i]:
#         dir = direct_list[i]
#         move = turn(move, dir)
#         i += 1
#         print('move', move)

#     # 뱀의 머리 부분에 사과가 있다면? 이전 위치를 추가하기.
#     if j < len(apple_x):   
#         if snake_x[0] == apple_x[j] and snake_y[0] == apple_y[j]:
#             snake_x.append(prev_x)
#             snake_y.append(prev_y) 

#             print('j:',j)
            
#             k += 1
#             j += 1
            
        

    

#     if (snake_x[0] < 1 and snake_x[0] > n) or (snake_y[0] < 1 and snake_y[0] > n):
#         break

    

# print(count)

# ----------------답지 확인 후-------------------------------------

n = int(input())
k = int(input())
data = [[0]*(n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2 :
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0

            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break   

        x, y = nx, ny

        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulate())

