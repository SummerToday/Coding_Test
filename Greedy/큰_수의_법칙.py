n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

count = m // (k+1) * k + m % (k+1)
sum = first * count + second * (m - count)

print(sum)