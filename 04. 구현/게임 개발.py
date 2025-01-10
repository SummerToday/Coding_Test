# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화 -> 2차원 리스트를 초기화 할 때는 컴프리헨션 문법 사용하는 것이 효율적.
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리 -> 추후 방문 여부를 확인해서 이동해야하기 때문.

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서로 이동했을 때의 각 성분 별 방향 변화량 설정 -> 방향을 설정해서 이동하는 문제일 경우 dx, dy 설정하는게 편함.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1 # bc 0 -> 1 -> 2 -> 3 시계방향으로 방향이 정의 되어있음. 
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1 # 방문 횟수
turn_time = 0 # 돌아간 횟수

while True:
    # 왼쪽으로 회전
    turn_left() # direction -= 1
    
    # 회전한 방향으로 이동했을 경우의 x, y 좌표.
    nx = x + dx[direction] 
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0: # 육지 and 가보지 않았을 경우.
        d[nx][ny] = 1 # 방문 여부 처리.
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
        
    # 네 방향 모두 갈 수 없는 경우 -> 왼쪽으로 4번 돌았을 경우 원래 방향으로 돌아옴.
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
            
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)


# 행위 별로 변하는 값들을 찾아내서 수치화 하기. 
# x, y 성분 분리하여 계산