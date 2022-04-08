# # 내가 풀이한 방법.. 틀림..
# x = int(input())

# n = 0

# def recursive_function(x, n):

#     if x == 1:
#         n += 1
#         return n
    
#     if x % 5 == 0:
#         x /= 5
#         n += 1
#         return recursive_function(x)
    
#     elif x % 3 == 0:
#         x /= 3
#         n += 1
#         return recursive_function(x)
    
#     elif x % 2 == 0:
#         x /= 2
#         n += 1
#         return recursive_function(x)

#     else: 
#         x -= 1
#         n += 1
#         return recursive_function(x)

# print(recursive_function(x, 0))

# # # ---------------------------------------------------------------------------

x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])

    
    

    
