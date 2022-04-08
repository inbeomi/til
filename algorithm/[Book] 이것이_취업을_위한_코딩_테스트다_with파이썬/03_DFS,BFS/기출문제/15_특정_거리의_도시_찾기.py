from collections import deque

n, m, k, x = map(int, input().split())
array = [[] for _ in range(n+1)]

for i in range(m):
    node, target = map(int, input().split())
    array[node].append(target)

# # # 여기 이후는 답지를 봄..

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()

    for next_node in array[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
    
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)


