# %%
# n개 -> p[n]원
# n개를 구매하기 위한 최댓값

# dp[i] = dp[i-k] + p[k]

n = int(input())
p = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(i):
        dp[i] = max(dp[i], dp[i-(k+1)] + p[k])

print(dp[-1])
# %%
