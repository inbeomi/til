N = int(input())

change = [500, 100, 50, 10]

money = N
coin = 0

for i in change:
    if money == 0:
        break
    coin += money // i
    money -= (money // i)*i

print(coin)

# # -------------책-----------------------------

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

