
n = input()
ten_list = [10**i for i in range(len(n))] # 1, 10, 100, ...

answer = 0
n = int(n)
for i in range(len(ten_list), 0, -1):
    count = n - ten_list[i-1] + 1
    n -= count
    answer += count*len(str(ten_list[i-1]))
    
print(answer)