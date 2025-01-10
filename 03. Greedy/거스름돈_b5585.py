n = int(input())
x = 1000 - n
y = 0
count = 0

coin_types = [500, 100 ,50, 10, 5, 1]

for coin in coin_types:
    y = x // coin
    count += y
    x -= coin * y

print(count)    
