# 11분/15분(성공)
n = int(input())
moveplan = list(input().split())

# L -> y -= 1
# R -> y += 1
# U -> x -= 1
# D -> x += 1
x = 1
y = 1
for i in range (len(moveplan)):
    if moveplan[i] == 'L' and y != 1:
        y -= 1
    elif moveplan[i] == 'R' and y != n:
        y += 1
    elif moveplan[i] == 'U' and x != 1:
        x -= 1
    elif moveplan[i] == 'D' and x != n:
        x += 1
print(x, y)
