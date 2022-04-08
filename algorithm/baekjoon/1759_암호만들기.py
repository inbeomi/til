# 최소 한 개의 모음(a, e, i, o, u)
# 최소 두 개의 자음

# 알파벳이 순서대로 배열되었을 것으로 추측

# 암호는 서로 다른 L개의 알파벳 소문자로 구성
# 암호 후보 문자의 종류 : C개

L, C = map(int, input().split())
candidate = sorted(input().split()) # 순서대로 알파벳 정렬

print(candidate)

answer = ''

def recursive(L, n, candidate):
    answer += candidate[n]

    if n == L:
        print(answer)
        return 
    recursive(L, n+1, candidate[n+1:])


for i in range(len(candidate[:-3])):
    answer = ''
    recursive(L, i, candidate)