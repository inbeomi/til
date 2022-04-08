# 최대공약수(Greatest Common Divisor, GCD): 

from itertools import combinations
from math import gcd
n = int(input())

for _ in range(n):
    answer = 0
    textcase = list(map(int, input().split()))[1:]
    for pair in combinations(textcase, 2):
        answer += gcd(*pair)
    print(answer)