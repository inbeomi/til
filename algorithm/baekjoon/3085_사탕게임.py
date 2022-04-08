# %%
n = int(input())

board = [list(input()) for _ in range(n)]

print(board)
# %%

def count(board):
    answer = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer,cnt)
        cnt = 1
        for j in range(1,n):
            d
            if  board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer,cnt)

    return answer




answer = 0
for i in range(n):
    for j in range(n):

        if j+1 < n:

            # 상하
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
            answer = max(answer, count(board))
            # 원래 상태로
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        
        if i+1 < n:

            # 좌우
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            
            answer = max(answer, count(board))
            # 원래 상태로
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)
# %%
