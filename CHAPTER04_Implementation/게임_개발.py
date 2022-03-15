# 68분/40분(애매한 성공, 제시된 test case만 실행해봄)
# 3번째 메뉴얼인 '바라보는 방향 유지한 채 한 칸 뒤로 가고 1단계로 돌아가기' 코드X
n, m = map(int,input().split())
a, b, d = map(int,input().split())
# gameMap 입력 고민만 15분
# 교재 참고
# gameMap = []
# for i in range(n):
#     gameMap.append(list(map(int, input().split())))
gameMap = [i for i in range(n)]
for i in range(n):
    gameMap[i] = list(map(int,input().split()))

direction = [-1, 1, 1, -1]

# 이동한 칸의 수
count = 1
# 현재 좌표 방문 처리
gameMap[a][b] = 1
rotation_count = 0
new_d = d

# 칸 이동을 위한 탐색 반복
while(True):
    # 왼쪽 방향으로 회전
    # 교재에선 따로 turn_left()로 써서 사용
    if d == 0:
        d += 3
    else:
        d -= 1
    rotation_count += 1
    
    # 한 바퀴 다 돌았으면
    if rotation_count == 4:
        # 교재 참고
        # 다 회전한 뒤 뒤로 갈 수 있다면 이동하고 뒤가 바다로 막혀있다면 break
        break

    # 회전한 방향의 좌표로 임시 이동
    new_a = a
    new_b = b
    if d % 2 == 0:
        new_a += direction[d]
    elif d % 2 == 1:
        new_b += direction[d]

    # 임시 이동한 곳이 육지인지 확인하고 실제로 이동
    # 교재 참고
    # 방문한 칸 저장용 배열(visited)과 육지와 바다를 표현한 전체 맵 표현용 배열(gameMap)을 따로 둠
    # if visited[a][b] == 0 and gameMap[a][b] == 0:
    # 회전한 이후 정면이 다 방문한 칸(visited == 1)이거나 바다(gameMap == 1)인 경우
    # else:
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
