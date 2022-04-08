n = int(input())




def recursive(n, start, end):
  

    if n == 1:
        print(start, end)
        return 

    else:
        recursive(n-1, start, 6-(start+end))
        print(start, end)
        recursive(n-1, 6-(start+end), end)

print(2**n-1)
recursive(n, 1, 3)