# 일단 의문이 드는 점은 뒤집을 때 연속된 숫자만을 뒤집거나, 전체를 뒤집거나
# 둘 중 하나만 가능하다는 건가임. 이것에 대해 명확하게 말해주지 않음.

S = input()

result0 = [v for v in S.split('1') if v] # 빈 칸을 없애주기 위함.
result1 = [v for v in S.split('0') if v]

if len(result0) > len(result1):
    # print(result1)
    print(len(result1))
else:
    # print(result0)
    print(len(result0))




