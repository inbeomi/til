n = int(input())
array = []
for i in range(n):
    temp = []
    for j in input().split():
        temp.append(int(j))
    array.append(temp)

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = array[i-1][j-1]
        
        if j == i:
            up = 0
        else:
            up = array[i-1][j]
        
        array[i][j] = array[i][j] + max(up_left, up)

result = 0
for i in range(n):
    result = max(result, array[n-1][i])

print(result)