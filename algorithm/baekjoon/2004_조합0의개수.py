from math import factorial

n, m = map(int, input().split())

# nCm = n!/(n-m)!m!
answer = int(factorial(n)/(factorial(n-m)*factorial(m)))
print(answer)
count = 0
for i in str(answer)[::-1]:
    if i == '0': count += 1
    else: break

print(count)

# nc0, nc1, nc2


# dp = [1] * 2000000001
# for i in range(len(dp)-1):
#     dp[i+1] = dp[i] * i

# answer = dp[n]/(dp[n-m]*dp[m])

# count = 0
# for i in str(answer)[::-1]:
#     if i == '0': count += 1
#     else: break

# print(count)