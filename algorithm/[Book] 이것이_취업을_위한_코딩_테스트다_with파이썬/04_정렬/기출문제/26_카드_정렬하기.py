# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))

# array.sort()

# sum = array[0] * (n-1)

# for i in range(1, len(array)):
#     n -= 1
#     sum += array[i]*n
    
# print(sum)

# # 답지에서 일부 힌트를 얻어 내가 문제의 맥락을 잘못 잡음을 깨달음
# # 결국 답지 봄.

import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one + two
    result += sum_value

    heapq.heappush(heap, sum_value)

print(result)


