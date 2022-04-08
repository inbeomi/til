current = list(map(int, input().split()))
add = int(input())

add_h = add // 60
add_m = add % 60

hour = current[0] + add_h
minute = current[1] + add_m

if minute > 59 :
    minute %= 60
    hour += 1

if hour > 23 :
    hour %= 24

print(hour, minute, end=' ')