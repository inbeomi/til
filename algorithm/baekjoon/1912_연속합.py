n = int(input())
# num_list = list(map(int, input().split()))

dp = [[] for _ in range(n)]
dp[0].extend(list(map(int, input().split())))
# print(dp)

for i in range(1, n):
    dp[i].extend([dp[i-1][j] + dp[0][j] for j in range(i, n)])

print(dp)
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
