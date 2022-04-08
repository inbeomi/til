loc = input()

ver = [str(i) for i in range(1,9)]
hor = ['a','b','c','d','e','f','g','h']

x = ver.index(loc[1]) + 1
y = hor.index(loc[0]) + 1

# method = ['unit'+ str(i) for i in range(1,9)]
value = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
# myzip = zip(method, value)
# mydict = dict(myzip)

count = 0

for i in range(len(value)):
    x += value[i][0]
    y += value[i][1]
    if 1 <= x <= 8 and 1 <= y <= 8:
        count += 1
    x -= value[i][0]
    y -= value[i][1]

print(count)
