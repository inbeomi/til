# # 내 풀이... 실패

# n, c = map(int, input().split())
# array = []
# for _ in range(n):
#     array.append(int(input()))


# def install(array, start, end, count):

#     if count == 0:
#         return 
    
#     mid = (start + end) // 2

#     count -= 1

#     install(array, start, mid, count)
#     install(array, mid, end, count)


# # # ---------------------------------답지를 보았다...----------------------------------

n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

# 범위의 최소값은 1이라는 것... 이게 책에 있는 내용과 다른 점..
start = 1
end = array[-1] - array[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1

    for i in range(1, n):
        if array[i] >= (value + mid):
            value = array[i]
            count += 1
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
    
print(result)
    