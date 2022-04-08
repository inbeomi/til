# n = int(input())
# dp = [1]* 1001

# count = 0

# def div_count(x, n, count):

#     if x % n == 0:
#         x //= n
#         count += 1
#         return div_count(x, n, count)

#     else:
#         return count

# for i in range(2, len(dp)):

#     if i % 2 == 0:
#         dp[i] = dp[i//2]*2
    
#     if i % 3 == 0:
#         dp[i] = dp[i//3]*3

#     if i % 5 == 0:
#         dp[i] = dp[i//5]*5

# # # -------------------답지 봄----------------------------------------------

n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    
    ugly[l] = min(next2, next3, next5)

    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2

    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
    
print(ugly[n-1])