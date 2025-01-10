N, K = map(int, input().split())
count = 0

while N >= K:
    # N이 K로 나누어떨어지지 않으면 1을 빼는 대신 한 번에 차이만큼 감소
    remain = N % K
    count += remain
    N -= remain
    
    N //= K
    count += 1

# 마지막으로 남은 N이 1이 될 때까지 처리
count += (N - 1)

print(count)
 