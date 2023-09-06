import math

def solution(progresses, speeds):
    answer = []
    day = []
    big_num = 0
    count = 0
    # 각 기능마다 배포까지 걸리는 day 수 계산
    for i in range(len(speeds)):
        day.append(math.ceil((100 - progresses[i])/speeds[i]))
    # 같이 배포할 기능들 걸러내기
    while True:
        if len(day) == 0:
            break
        big_num = day.pop(0)
        count = 1
        while True:
            if len(day) == 0:
                answer.append(count)
                break
            if big_num >= day[0]:
                count += 1
                day.pop(0)
            else:
                answer.append(count)
                break
    return answer
