from itertools import combinations

while True:
    inputs = list(map(int, input().split()))

    if inputs[0] == 0:
        break

    for case in combinations(inputs[1:], 6):
        print(" ".join(map(str, case)))
    
    print()

# combinations 라이브러리 활용하여 접근함
# join을 사용할 때, 리스트 내부의 값은 문자형이이어야 함