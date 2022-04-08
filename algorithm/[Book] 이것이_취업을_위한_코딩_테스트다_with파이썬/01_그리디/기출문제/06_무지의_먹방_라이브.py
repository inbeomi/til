# 일단 음식을 순서대로 먹을 수 있게 반복할 수 있는 구문이 필요함
# 몇 번? K번. 단 음식의 종류를 고려해야 함.

# 답안지를 확인함. 

# food_times = list(map(int, input().split()))
# k = int(input())

# i = 0

# for _ in range(k):
#     if food_times[i] == 0:
#         i += 1

#     food_times[i] -= 1
#     i += 1
#     print(food_times)

#     if i == len(food_times):
#         i = 0
    
#     if max(food_times) == 0:
#         print(-1)
#         break

# print(i+1)

def solution(food_times, k):

    foods = []
    n = len(food_times)

    for i in range(n):
        foods.append((food_times[i], i+1))

    foods.sort()

    pretime = 0

    for i, food in enumerate(foods):
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key = lambda x: x[1])
                return sublist[k][1]
        
        n -= 1

    return -1

    
    
    
    