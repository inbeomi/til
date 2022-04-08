# # n = int(input())
# # number_list = list(map(int, input().split()))
# # plus, minus, multiple, dividend = map(int, input().split())

# # 지금 드는 생각. 아니 내가 문제를 끝까지 붙잡지 않아서 못푸는 건가
# # 아니면 그냥 문제 자체가 어려운 건가. 쉽지 않구만
# # 어떻게 접근해야할 지 감 자체가 안오는
# # # # -------------------------------------------------------------

# # from itertools import product # 중복 순열 라이브러리

# # n = 4
# # print(list(product(['+', '-', '*', '/'], repeat = (n-1))))
# # -----------------------------------------------------------------
# # from itertools import permutations

# # data = ['A', 'B', 'C']

# # result = list(permutations(data, 3))

# # print(result) 
# # # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
# # -------------------------------------------------------------------
# # from itertools import combinations

# # data = ['A', 'B', 'C']
# # result = list(combinations(data, 2))

# # print(result) #[('A', 'B'), ('A', 'C'), ('B', 'C')]
# # -------------------------------------------------------------------
# # from itertools import product

# # data = ['A', 'B', 'C']
# # result = list(product(data, repeat=2))

# # print(result)
# # # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
# # ----------------------------------------------------------------------------
# # from itertools import combinations_with_replacement

# # data = ['A', 'B', 'C']
# # result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)

# # print(result)
# # # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
# # # # -----------------------------------------------------


# # answer = number_list[0]

# # def max(n, plus, minus, multiple, dividend):

# #     for i in range(1, len(number_list)):
        
# #         for i in range(len(plus)):
# #             plus -= 1
# #             answer 
# #             max(answer, plus, minus, multiple, dividend)


# #         pass

# # def min():
# #     pass

# # for i in range(1, len(number_list)):
    
# # # # --------------------------정답 봄----------------------------------------------------

# n = int(input())
# data = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())

# min_value = 1e9
# max_value = -1e9

# def dfs(i, now):
#     global min_value, max_value, add, sub, mul, div

#     if i == n:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)

#     else:
#         if add > 0:
#             add -= 1
#             # 한 층 깊이 들어갔다가 계산하고
#             dfs(i+1, now + data[i])
#             # 거꾸로 한 층 위로 나오는 모습이 그려짐
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i+1, now - data[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i+1, now * data[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i+1, int(now /data[i]))
#             div += 1

# dfs(1, data[0])

# print(max_value)
# print(min_value)

# # # ---------------------------------------------------------------------------------

# 핵심은 계속 파고들면서 계산을 하게 되는데, 언제까지 파고들어야 하는지. 그리고 파고들면서 계산해야 하는 값이 무엇인지 생각하면서 접근할 것
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

minimum = 1e9
maximum = -1e9

def dfs(i, now):

    global minimum, maximum, add, sub, mul, div
    
    if i == n:
        minimum = min(now, minimum)
        maximum = max(now, maximum)

    else:
    
        if add > 0:
            add -= 1
            dfs(i+1, now+numbers[i])
            add += 1
        
        if sub > 0:
            sub -= 1
            dfs(i+1, now-numbers[i])
            sub += 1
        
        if mul > 0:
            mul -= 1
            dfs(i+1, now*numbers[i])
            mul += 1
        
        if div > 0:
            div -= 1
            dfs(i+1, int(now/numbers[i]))
            div += 1

dfs(1, numbers[0])

print(maximum)
print(minimum)