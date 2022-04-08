N = int(input()) # 모험가의 수
X = list(map(int, input().split())) # 각 모험가의 공포도의 값

X.sort() # 오름차순 정리

group = 0
group_list = []

for i in X:
    group_list.append(i) # 그룹 바구니에 인원 1명씩 추가

    if len(group_list) == i:
        group += 1 # 한 그룹 생성
        group_list = [] # 그룹 바구니 리셋
    
print(group)