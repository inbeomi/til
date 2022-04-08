# # 건들지도 못함ㅎ

# 현재 구조물이 설치 가능한 지 확인하기
def possible(answer):
    for x, y, stuff in answer:
        # 기둥일 경우
        if stuff == 0:
            if y == 0 or [x-1,y,1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        # '보'인 경우
        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False    
        return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            print('append', answer)
            if not possible(answer):
                print('remove', answer)
                answer.remove([x, y, stuff])
    return answer.sort()

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(5, build_frame))
# array = [0]

# array.append([1,2,3])

# print(array)