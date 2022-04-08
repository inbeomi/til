from collections import deque

n = int(input())
queue = deque()

def output(cmd, queue):

    if cmd == 'pop' and queue:
        return queue.popleft()
    elif cmd == 'front' and queue:
        return queue[0]
    elif cmd == 'back' and queue:
        return queue[-1]
    else:
        return -1
        

for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().rstrip().split()))

    if cmd[0] == 'push':
        queue.append(int(cmd[1]))

    elif cmd[0] == 'size':
        print(len(queue))

    elif cmd[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    else:
        print(output(cmd[0], queue))

        

    