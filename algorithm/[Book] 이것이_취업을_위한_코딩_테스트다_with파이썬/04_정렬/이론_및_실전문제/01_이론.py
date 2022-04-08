# # 선택 정렬 소스코드
# source = [7, 5 ,9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(source)):
#     min_index = i
#     for j in range(i+1, len(source)):
#         if source[min_index] > source[j]:
#             min_index = j
#     source[i], source[min_index] = source[min_index], source[i]

# print(source)

# # # ---------------------------------------------------------------

# # 상입 정렬 소스코드

# for i in range(1, len(source)):
#     for j in range(i, 0, -1):
#         if source[j] < source[j-1]:
#             source[j], source[j-1] = source[j-1], source[j]
#         else:
#             break

# print(source)

# #  상입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작함

# # # ---------------------------------------------------------------

# # 큌 정렬 소스코드

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start  and array[right] >= array[pivot]:
#             right -= 1
        
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]

#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)  

# quick_sort(array, 0, len(array)-1)
# print(array)

# # # ---------------------------------------------------------------

# # 파이썬의 장점을 살린 큌 정렬 소스코드

# def quick_sort(array):

#     if len(array) <= 1:
#         return array

#     pivot = array[0]
#     tail = array[1:]

#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]

#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))

# # # ---------------------------------------------------------------

# # 계수 정렬 소스코드

# array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ')

# # 항상 사용할 수 있는 정렬 알고리즘은 아니며, 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합함.
# # 즉, 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을수록 유리함.

# # # ---------------------------------------------------------------

# # py sorted, sort 소스코드

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted(array)
# print(array)

# result = sorted(array)
# print(result)

# array.sort()
# print(array)

# # # ---------------------------------------------------------------

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

