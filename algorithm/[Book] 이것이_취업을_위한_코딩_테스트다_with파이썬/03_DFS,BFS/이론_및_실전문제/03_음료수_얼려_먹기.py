# # 일단 어떻게 구현할 지 감이 안왔음..
# n, m = map(int, input().split())

# ice_shape = [[list(input())] for i in range(n)]
# ice_base = [[0]*m for i in range(n)]

# print(ice_shape)
# print(ice_base)

# # # -----------------------------------------------------------------------

# # py 답안 예시

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
        
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            print(f'({i},{j})', "True")
            result += 1

print(result)

# # 일단 깊이 우선 탐색... 쉽지 않지만 일단은 재귀함수가 들어가면 해당 경로를 다 맞쳐야만 다른 경로를
# # 훓어본다는 것만을 생각해보면 얼추 맞는 듯.