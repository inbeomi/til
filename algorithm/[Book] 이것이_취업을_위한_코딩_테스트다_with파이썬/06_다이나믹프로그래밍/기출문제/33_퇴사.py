# # # 내 풀이 실패..ㅠ
# n = int(input())
# array = []
# for i in range(n):
#     array.append(input().split())

# dp = [0]*(n+1)

# for i in range(1, n+1):

#     if i+1 >= (array[i][0] + i):
#         dp[i+1] = dp[i+1] + 
#     else:
#         continue

#     dp[i] = dp[i-1]

# # # ------------------------답지 봄------------------------------------------------------

n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + i
    
    if time <= n:
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    
print(max_value)