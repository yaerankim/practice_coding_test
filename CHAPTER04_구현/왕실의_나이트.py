# 25분/20분(개띨빵한 실패)
inputc = list(input())
c = inputc[0]
n = int(inputc[1])

count = 0
two = [+2, -2]
one = [+1, -1]

for i in range (2):
    for j in range (2):
        if 1 <= n+one[i] <= 8 and ord("a") <= ord(c)+two[j] <= ord("h"):
            count += 1
        # elif가 아니라 if인데 elif라고 해서 더 나와야 할 경우의 수가 반절정도밖에 나오지 않음
        # elif 1 <= n+two[i] <= 8 and ord("a") <= ord(c)+one[j] <= ord("h"):
            # count += 1
        if 1 <= n+two[i] <= 8 and ord("a") <= ord(c)+one[j] <= ord("h"):
            count += 1
print(count)
