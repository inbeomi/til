# # py 순차 탐색 소스코드

# def sequential_search(n, target, array):
#     for i in range(n):
#         if array[i] == target:
#             return i + 1

# print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]

# print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# array = input().split()

# print(sequential_search(n, target, array))

# # # ----------------------------------------------------------------------------------

# # 이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘. 
# # 데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있다는 특징이 있음.

# # py 재귀 함수로 구현한 이진 탐색 소스코드

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2

#     if array[mid] == target:
#         return mid

#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
    
#     else:
#         return binary_search(array, target, mid+1, end)

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == "None":
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result+1)

# # # ----------------------------------------------------------------------------------

# # py 반복문으로 구현한 이진 탐색 소스코드

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

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == "None":
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result+1)

# # 처리해야 할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN)의 속도를 내야 하는 알고리즘 사용할 것.

# # # ----------------------------------------------------------------------------------

# # 한 줄 입력받아 출력하는 소스코드

import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)
