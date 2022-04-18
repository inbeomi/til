from collections import deque

K = int(input())

def bfs(start, graph, visited):
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            else:
                return False
    
    return True

for i in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for j in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    if bfs(1, graph, visited):
        print('YES')
    else:
        print('NO')

# 