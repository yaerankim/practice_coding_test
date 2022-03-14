# page 92
# 30분/30분(시간 넘겨 성공)
# BUT a 배열의 입력을 한 줄로 받지 못한 잘못된 입력을 개선할 필요가 있음
# 답안 코드의 sort()를 참고하였는데
# 처음에 max()를 사용하고 이후에 for문을 이용해서 다음 max 값을 찾는 방식을 떠올림 -> 더 복잡한 방식
n, m, k = map(int, input().split())

# 내가 생각한 a 입력받기(문제의 입력 방식과 다름)
# a = []
# for _ in range (n):
#     num= int(input())
#     a.append(num)

# 답안 참고한 입력 방식
a = list(map(int, input().split()))

a.sort(reverse=True)
first_max = a[0]
next_max = a[1]

sum = 0
count = 1
for _ in range (m):
    if count == k:
        count = 0
        sum += next_max
    else:
        sum += first_max
        count += 1
print(sum)
