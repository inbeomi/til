N, M = map(int, input().split())

matrix = list()
minimum_list = []
for i in range(N):
    column = list(map(int, input().split()))
    matrix.append(column)

for i in range(N):
    test = min(matrix[i])
    minimum_list.append(test)

print(max(minimum_list))
        