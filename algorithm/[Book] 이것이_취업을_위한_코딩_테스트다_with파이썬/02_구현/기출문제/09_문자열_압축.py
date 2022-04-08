# 일단 몇 개로 자를 수 있는지부터 알아야 하고.
# 자른 것을 기준으로 갯수를 세어야 함.
# 갯수를 세서 그것을 비교하면 될 듯.
# 프로그래머스에 제출하니 96/100점임. 하나 런타임 에러..
# -> 문자열이 하나일 때의 구문을 추가해줬더니 통과...ㅠ

def solution(s):

    n = len(s)

    # div = []

    # for i in range(1,n):
    #     if n % i == 0:
    #         div.append(i)

    
    answer_list = []
    
    # 나눌 수 있는 수들로 반복적으로 실행
    for i in range(1,n):

        str_list = []
        # 일단 글씨를 나눔
        for j in range(0, n, i):
            str_list.append(s[j:j+i])
        
        # 나눈 글씨들을 세기 시작함
        count = 1
        cut_list = []
        for i in range(0, len(str_list)-1):
    
            if str_list[i] == str_list[i+1]:
                count += 1

            else:
                cut = str(count) + str_list[i]
                if count == 1:
                    cut = str_list[i]
                cut_list.append(cut)
                count = 1
                
                    
            if i == len(str_list)-2:
                cut = str(count) + str_list[i+1]
                if count == 1:
                    cut = str_list[i+1]
                cut_list.append(cut)
        
        print(cut_list)

        ans = ''.join(cut_list)
        answer_list.append(len(ans))
    
    answer = min(answer_list)

    # print(div)
    print(answer_list)

    return answer

print(solution("abcabcdede"))