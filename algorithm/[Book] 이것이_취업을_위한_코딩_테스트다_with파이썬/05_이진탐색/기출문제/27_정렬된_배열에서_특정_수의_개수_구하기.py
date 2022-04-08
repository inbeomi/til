# from bisect import bisect_left, bisect_right

# a = [1, 2, 4, 4, 8]
# x = 4

# # 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# print(bisect_left(a,x))
# # 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# print(bisect_right(a,x))

# from bisect import bisect_left, bisect_right

# def count_by_range(a, left_value, right_value):
# 	right_index = bisect_right(a, right_value)
# 	left_index = bisect_left(a, left_value)
# 	return right_index - left_index

# a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# print(count_by_range(a, 4, 4))

# print(count_by_range(a, -1, 3))

# # # -------------------------------------------------------------------------
# from bisect import bisect_left, bisect_right

# n, x = map(int, input().split())

# array = list(map(int, input().split()))

# def answer(array, x):
    
#     right_index = bisect_right(array, x)
#     left_index = bisect_left(array, x)

#     if right_index - left_index == 0 :
#         return -1
#     else:
#         return right_index - left_index

# print(answer(array, x))

# # # -------------------------------------------------------------------------

def first(array, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if (mid == 0 or array[mid-1] < target) and array[mid]== target:
            return mid

        if array[mid] >= target:
            end = mid -1
        else:
            start = mid + 1
        
    return None

def last(array, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if (mid == n-1 or array[mid+1] > target) and array[mid] == target:
            return mid

        if array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
        
    return None

def count(array, x):

    n = len(array)

    a = first(array, x, 0, n-1)

    if a == None:
        return 0
    
    b = last(array, x, 0, n-1)

    return b-a+1


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count(array, x)

if count == 0:
    print(-1)
else:
    print(count)