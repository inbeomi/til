# # 내 답안.. 실패..
# n, m = map(int, input(),split())
# array = list(map(int, input().split()))

# array.sort()

# def cut_height(array, m, start, end):

#     mid = (start + end) // 2

#     cut = array[mid]

#     all_cut = [x-cut for x in array[start, mid]]

#     if sum(all_cut) >= m:
#         end = mid

# # # ---------------------------------------------------------------------

n, m = list(map(int, input(),split()))
array = list(map(int, input().split()))

start = 9
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid :
            total += x - mid
        
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
        