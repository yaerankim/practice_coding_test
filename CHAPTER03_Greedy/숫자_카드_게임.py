# page 96
# 12분(실패)
# n, m = map(int, input().split())
# for i in range (n):
#     for j in range (m):
#         a[i][j] = int(input())

# for i in range (n):
#     min_num[i] = min(a[i][j for j in range m])
    
# max_num = max(min_num[i for i range n])

# print(max_num)

# 답안 코드 참고한 후 다시 작성해보기
# min() 사용한 방식
n, m = map(int, input().split())

max_num = 0
for i in range (n): # 행별로 반복
    a = list(map(int, input().split()))
    min_num = min(a) # min(), max()에 list 자체를 인자로 넣는 것도 가능하다
    if min_num > max_num:
        max_num = min_num
    # 또는
    # max_num = max(max_num, min_num)
    
print(max_num)
