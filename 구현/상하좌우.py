a =  int(input())

x, y = 1, 1

moving = list(map(str, input().split()))

for i in range(len(moving)):
    if moving[i] == 'L':
        if x != 1:
            x -= 1
    if moving[i] == 'R':
        if x != a:
            x += 1
    if moving[i] == 'U':
        if y != 1:
            y -= 1
    if moving[i] == 'D':
        if y != a:
            y += 1        

print(x, y)            

