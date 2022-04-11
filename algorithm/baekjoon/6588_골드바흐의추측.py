import math
import sys

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def split_to_prime(n):
    for i in range(3, n-2):
        if prime(i) and prime(n-i):
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        split_to_prime(n)

# 소수를 판명하는 함수와, 수를 2개의 소수로 분리하는 함수를 만듦
