import sys
all_s = set([str(x) for x in range(1, 21)])

def add(cmd):
    global S
    if cmd[1] in S:
        pass
    else:
        S.add(cmd[1])
    
def remove(cmd):
    global S
    if cmd[1] in S:
        S.remove(cmd[1])
    else:
        pass

def check(cmd):
    global S
    if cmd[1] in S:
        print(1)
    else:
        print(0)

def toggle(cmd):
    global S
    if cmd[1] in S:
        S.remove(cmd[1])
    else:
        S.add(cmd[1])

def all(cmd):
    global S
    S = all_s

def empty(cmd):
    global S
    S = set()

function = {'add' : add,
            'remove' : remove,
            'check' : check,
            'toggle' : toggle,
            'all' : all,
            'empty' : empty}

M = int(input())

S = set()
for _ in range(M):
    cmd = sys.stdin.readline().split()
    function[cmd[0]](cmd)
    