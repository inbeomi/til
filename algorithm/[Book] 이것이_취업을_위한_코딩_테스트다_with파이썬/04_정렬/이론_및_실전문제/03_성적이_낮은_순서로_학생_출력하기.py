n = int(input())

array = []

for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

# def key(data):
#     return data[1]

array.sort(key=lambda data : data[1])

for i in range(len(array)):
    print(array[i][0], end=' ')