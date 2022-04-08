s = input()

string = []
number = []

for i in range(len(s)):
    if 65 <= ord(s[i]) and ord(s[i]) <= 90:
        string.append(s[i])
        # print(string)
    else:
        number.append(int(s[i]))
        # print(number)

string.sort()
# print(string)
# print(number)

print(''.join(string) + str(sum(number)))
