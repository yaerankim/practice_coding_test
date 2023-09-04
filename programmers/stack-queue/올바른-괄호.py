def solution(s):
    answer = True
    stack = list()
    for i in s:
        if i == '(':
            stack.append(i)
        else: # s == ')'인 상황
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) != 0:
        answer = False
    return answer