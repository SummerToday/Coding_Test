a = int(input())

x, y, z = 24, 60, 60

count = 0

for l in range(a+1):
    for i in range(y):
        for k in range(z):
            if '3' in str(l) + str(i) + str(k):
                count += 1

print(count)