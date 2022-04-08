num = list(map(int, input().split()))
num_list = [0]*7

for i in num:
    num_list[i] += 1

if max(num_list) == 3:
    i = num_list.index(3)
    print(10000 + i*1000)
elif max(num_list) == 2:
    i = num_list.index(2)
    print(1000 + i*100)
else:
    num.sort(reverse=True)
    print(num[0]*100)