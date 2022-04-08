def solution(lottos, win_nums):
    
    rank = [6, 6, 5, 4, 3, 2, 1, 1, 1]
    
    check_count = 0
    for win_num in win_nums:
        if win_num in lottos:
            check_count += 1
            
    zero_count = 0     
    for lotto in lottos:
        if lotto == 0:
            zero_count += 1
    answer = [rank[check_count+zero_count], rank[check_count]]
    
    return answer