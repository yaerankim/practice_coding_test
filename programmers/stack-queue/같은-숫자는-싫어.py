def solution(arr):
    answer = []
    temp = []
    before_num = -1
    while arr:
        if before_num == arr[-1]:
            arr.pop()
        else:
            temp.append(arr.pop())
            before_num = temp[-1]
    while temp:
        answer.append(temp.pop())
    return answer