a = int(input())

x, y, z = 24, 60, 60

count = 0

for l in range(a+1):
    for i in range(y):
        for k in range(z):
            if '3' in str(l) + str(i) + str(k):
                count += 1

print(count)



'''
for i in range(x):
    if i % 3 == 0:
        countX += 1
    for k in range(y):
        if k % 3 == 0:
            if (count)
            countY += 1
        for p in range(y):  
            if p % 3 == 0:
                countZ += 1
'''
 