# # 내 풀이방식 

# n = int(input())
# n_list = list(map(int, input().split()))

# m = int(input())
# m_list = list(map(int, input().split()))

# n_list.sort()

# def binary_search(array, target, start, end):
#     if start > end:
#         return None

#     mid = (start + end) // 2
    
#     if start == end and array[mid] != target:
#         return "No"
    
#     if array[mid] == target:
#         return "Yes"

#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
        
#     else:
#         return binary_search(array, target, mid+1, end)

# for i in m_list:
#     print(binary_search(n_list, i, 0, n-1), end=' ')

# # # ----------------------------------------------------------------------------------------------

# # py 답안 예시(이진 탐색)

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2

#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# n = int(input())
# array = list(map(int, input().split()))
# array.sort()

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     result = binary_search(array, i, 0, n-1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# # 'no'가 안나오는데?? 아... None 이 아니라 'None'을 입력했네..
# # 2 3 7 8 9 
# # 5는? 0,4  0,1  1,1  2,1

# # # ----------------------------------------------------------------------------------------------

# # py 답안 예시(계수 정렬)

# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# # # ----------------------------------------------------------------------------------------------

# # py 답안 예시(집합 자료형 이용)

# n = int(input())
# array = set(map(int, input().split()))
# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if i in array:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# # 훨씬 더 간단하지만 만약에 데이터 개수가 엄청 많다면 이진 탐색으로 접근하는 생각이 필요하다..

