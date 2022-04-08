# 일단은 회전하는 것, 이동하는 것에 대한 로직을 짜줘야 함.
# 그리고 어디에 값이 비워져 있는지를 추출해야 함.
# 그런데 홈과 돌기가 딱 맞는다는 상황을 어떻게 구현할 것인가가 문제.
# 심지어 키와 자물쇠의 크기는 다를 수 있음. 이 상황도 고려.
# 그렇다면 열쇠의 경우 크기에 상관없이 회전하거나 움직일 수 있어야

# 생각해보니깐 굳이 일일이 다 돌려볼 필요는 없는 듯. 
# 비워있는 값 간의 관계만 동일하면 되잖음? 

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

# def find_loc(list, num):
#     find = []
#     for i in range(len(list)):
#         for j in range(len(list[i])):
#             if list[i][j] == num:
#                 find.append((i, j))
#     return find

def turn_90(list):

    n = len(list)
    result = [[0]*n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = list[i][j]
    return result

    


def move(list, ):
    pass

def solution(key, lock):
    answer = True
    return answer
print(key)
print(turn_90(key))
