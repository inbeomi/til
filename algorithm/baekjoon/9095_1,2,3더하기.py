# Fail
from itertools import combinations

n = int(input())

def combination(num):
    temp = [0]*(num-1)
    answer = 0
    for i in range(1, num):
        answer += len(list(combinations(temp, i)))
    return answer

for _ in range(n):
    num = int(input())
    print(combination(num))