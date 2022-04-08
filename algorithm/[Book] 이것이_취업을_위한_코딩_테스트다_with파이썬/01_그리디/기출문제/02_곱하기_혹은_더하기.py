# 0, 1 은 더하고, 나머지는 곱하면 가장 큰수를 만들 수 있음
# 그러나 처음값이 1 이하라면 무슨 값이 나와도 값을 더해줘야 함.

S = input() # 문자열로 입력

answer = int(S[0]) # 기준점 생성 및 정답 변수

for i in range(1, len(S)):
    
    if int(S[i]) == 0 or int(S[i]) == 1:
        answer += int(S[i])
    else:
        if answer <= 1: 
            answer += int(S[i])
        else:
            answer *= int(S[i])

print(answer)