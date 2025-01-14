from collections import deque # BFS 구현

n, m = map(int, input().strip())

graph = []

for _ in range(n):
    graph.append = map(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 메서드 정의
def bfs(x, y):
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 큐에서 하나의 원소를 뽑아 출력
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

print(bfs(0,0))
    
            