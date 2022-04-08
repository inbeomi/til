# 순열로 접근하려다가 목차의 목적과 맞지 않은 거 같아서
# 답지를 보고 다시 작성함

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                count += 1

print(count)