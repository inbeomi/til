# 답안지 확인하고 품.
# 1부터 target-1 까지의 모든 금액을 만들 수 있다는 것을 알아차리면 됨.

N = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for i in data:
    if target < i:
        print(target)
        break
    target += i

print(target)

# 1 2 4