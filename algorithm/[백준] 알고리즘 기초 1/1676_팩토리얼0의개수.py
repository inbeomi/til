n = int(input())

# 값을 저장할 공간 설정
dp = [1]*501 

def factorial(n):
    if n <= 1:
        return 1

    dp[n] = factorial(n-1) * n

    return dp[n]

print(factorial(15))

count = 0
for i in str(factorial(n))[::-1]:
    if i == '0':
        count += 1
    else:
        break

print(count)

