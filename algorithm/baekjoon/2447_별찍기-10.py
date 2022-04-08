n = int(input())

star = [['*']*n for _ in range(n)]

def recursive_function(n, x, y):
    
    nn = n // 3

    for i in range(nn):
        for j in range(nn):
            star[x-nn//2+i][y-nn//2+j] = ' '

    if n == 3:
        star[x][y] = ' '
    
    else:
        for i in range(-1,2):
            for j in range(-1,2):             
                recursive_function(nn, x+(nn*i), y+(nn*j))

        

recursive_function(n, n//2, n//2)

for row in star:
    print(''.join(row))