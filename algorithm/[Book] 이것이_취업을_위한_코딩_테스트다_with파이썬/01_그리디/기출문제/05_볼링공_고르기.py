n, m = map(int, input().split())
weight = list(map(int, input().split()))

unique = list(set(weight))

all = n*(n-1)/2

for i in unique:
    count = weight.count(i)
    delete = count*(count-1)/2
    all -= delete

print(int(all))
