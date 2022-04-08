new_id = "...!@BaT#*..y.abcdefghijklm"

# 모든 단계를 일일이 구현해야 하는 문제

# 모든 단계를 일일이 구현해야 하는 문제

special = ['-', '_', '.']

def solution(new_id):
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    temp = ''
    for i in new_id:
        if i.isalnum() or i in special: # isalnum()... ()를 꼭 넣자.
            temp += i
    new_id = temp
    
    # 3단계
    temp = new_id[0]
    for i in range(1, len(new_id)):
        if new_id[i] == '.' and temp[-1] == '.':
            continue
        else: 
            temp += new_id[i]
    new_id = temp
    
    # 4단계 -> 제한사항에서 걸림. 데이터가 한 개 있는 경우가 있어서..!
    if len(new_id) >= 2:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    else:
        if new_id == '.':
            new_id = ''
            
    # 5단계
    if new_id == '':
        new_id = 'a'
        
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
    # 7단계
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    
        
    return new_id
