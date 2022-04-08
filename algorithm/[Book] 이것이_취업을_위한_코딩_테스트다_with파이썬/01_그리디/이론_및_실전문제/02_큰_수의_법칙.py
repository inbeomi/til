N, M, K = map(int, input().split())
number = list(map(int, input().split()))

number.sort(reverse=True)
result = 0
m = 0

print(number)

for i in range(M):
    if m < K:
        result += number[0]
        m += 1

    else:
        result += number[1]
        m = 0

print(result)

