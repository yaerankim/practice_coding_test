# 68분/40분(아마 성공)
n, m = map(int,input().split())
a, b, d = map(int,input().split())
gameMap = [i for i in range(n)]
for i in range(n):
    gameMap[i] = list(map(int,input().split()))

direction = [-1, 1, 1, -1]

count = 1 # 이동한 칸의 수
gameMap[a][b] = 1 # 이미 서 있는 곳 다시 방문 안 하도록 수정
rotation_count = 0
new_d = d

# 한 번의 칸 이동을 위한 탐색 반복
while(True):
    # 왼쪽 방향으로 회전
    if d == 0:
        d += 3
    else:
        d -= 1
    rotation_count += 1
    
    # 한 바퀴 다 돌았으면
    if rotation_count == 4:
        break

    # 회전한 방향의 좌표로 임시 이동
    new_a = a
    new_b = b
    if d % 2 == 0:
        new_a += direction[d]
    elif d % 2 == 1:
        new_b += direction[d]

    # 임시 이동한 곳이 육지인지 확인하고 실제로 이동
    if gameMap[new_a][new_b] == 0:
        if d % 2 == 0:
            a += direction[d]
        elif d % 2 == 1:
            b += direction[d]
        count += 1 # 해당 칸 방문
        # 방문 등록
        gameMap[a][b] = 1
        # 회전 수 초기화
        rotation_count = 0
        
print(count)
