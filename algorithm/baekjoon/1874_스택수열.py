import sys
from collections import deque

n = int(input())

target = []
for _ in range(n):
    target.append(int(input()))

stack = deque()
stack.extend([x for x in range(1, n+1)])

bin_stack = []
for t in target:
    while t != stack[-1]:
        bin_stack.append(stack.popleft())
        print('+')

n = int(input())

stack = []
answer = []
cnt = 1

def test():

    global stack, answer, cnt

    for _ in range(n):
        num = int(input())

        while cnt <= num:
            stack.append(cnt)
            answer.append('+')
            cnt += 1

        if stack[-1] == num:
            stack.pop()
            answer.append('-')
        else:
            return False
    
    return True

if test():
    print('\n'.join(answer))
else:
    print('NO')
        

        