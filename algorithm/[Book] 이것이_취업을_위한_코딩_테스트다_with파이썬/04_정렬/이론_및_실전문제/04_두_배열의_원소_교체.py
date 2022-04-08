n, k = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort()

for i in range(k):
    if A[i] < B[-i]:
        A[i], B[-i] = B[-i], A[i]
    else:
        break

print(sum(A))