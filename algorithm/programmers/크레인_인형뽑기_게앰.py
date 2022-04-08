# board는 최대 900칸
# 인형의 종류는 최대 100개
# 작동 횟수(moves)는 최대 1000번

# moves에서 하나를 뽑음. 이후 해당하는 인덱스에 맞는 값을 Board에서 뽑아야 됨.
# 그런데 board 구성이 뽑기 어렵게 되어 있는 듯? -> 다시 뽑기 편하게 구성해줌
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def new_board(board):

    n = len(board)
    new_board = [[] for _ in range(n)]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0:        
                new_board[j].append(board[i][j])
    
    return new_board


def solution(board, moves):
    
    # 담을 공간 생성
    box = [0]
    count = 0
    # 뽑기 편하게 데이터 마련하기
    board = new_board(board)

    # 차례대로 뽑음
    for i in moves:
        # 인덱스 맞춰주기
        if board[i-1] == []:
            continue
        else:
            doll = board[i-1].pop(0)
            if box[-1] == doll:
                count += 2
                box.pop()
            else:
                box.append(doll)

    return count

print(solution(board, moves))