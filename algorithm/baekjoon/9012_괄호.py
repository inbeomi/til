n = int(input())

def check(text):
    cnt = 0
    for t in text:
        if cnt < 0:
            return False

        if t == ")": 
            cnt -= 1
        elif t == "(": 
            cnt += 1
        else: 
            continue
    
    if cnt == 0:
        return True
    else:
        return False


for _ in range(n):
    if check(input()):
        print("YES")
    else:
        print("NO")
