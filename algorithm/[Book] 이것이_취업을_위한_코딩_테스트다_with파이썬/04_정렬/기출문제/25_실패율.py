# 결과적으로 스테이지의 번호를 출력해야 함.

def solution(N, stages):

    round = [0] * (N+2)
    all = len(stages)
    box = []

    for each in stages:
        round[each] += 1

    for i in range(1, len(round)-1):
        count = round[i]/all
        all -= round[i]
        box.append((i, count))

    box.sort(key=lambda x : -x[1])

    answer = [x[0] for x in box]
    return answer

N = 4
stages = [4,4,4,4,4]

print(solution(N, stages))

# # ------런타임 에러....몇 개가 존재함.. ---------------------------

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count/length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda x : x[1], reverse = True)

    answer = [i[0] for i in answer]

    return answer




