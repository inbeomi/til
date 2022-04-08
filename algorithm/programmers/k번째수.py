# 입력값이 각각 최대 100개로 한정됨

# array를 짤라야 함. command의 i,j를 기준으로
# 그리고 정렬하기
# 그 중에서 K번째 수를 뽑아서 한 리스트에 보관하기

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):

    answer = []

    for command in commands:
        
        i, j, k = command # Unpacking
        cut_array = array[i-1:j] # 이 때 리스트의 마지막 값을 넣는 것에 주의!
        cut_array.sort()
        answer.append(cut_array[k-1])

    return answer

print(solution(array, commands))