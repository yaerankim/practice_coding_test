# 13분/15분(실패)
# if h == 3 or m == 3 or s == 3: 가 잘못됨
# 그냥 일의 자리 수 3이나 3의 배수를 찾는게 아니라 3이 하나라도 들어가는지 이므로
# 문자열로 파악하는 게 맞음
# if m == 59: m = 0 도 필요없는 코드
# 없어도 알아서 3중 반복문이 잘 돌아감
n = int(input())
count = 0
for h in range (n + 1):
    if m == 59:
        m = 0
    for m in range (60):
        if s == 59:
            s = 0
        for s in range (60):
            # if h == 3 or m == 3 or s == 3:
            #    count += 1
            if '3' in str(h) + str(m) + str(s):
                count += 1
print(count)
