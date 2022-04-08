s = "one4seveneight"

word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):

    global word

    for idx, num in enumerate(word):
        if num in s:
            s = s.replace(num, str(idx))

    answer = s
    return answer


print(solution(s))

help(replac)