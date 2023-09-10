def solution(prices):
    answer = []
    # 1) 정확성 66.7, 효율성 33.3, 100/100(40분)
    # "몇 초 후에 가격이 떨어지는가"에 초점을 두고 풀었을 때 해결
    # 효율성 ~159.77ms, 19.5MB
    for i in range(len(prices)-1):
        t = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                t += 1
            elif prices[i] > prices[j] and t != 0:
                t += 1
                break
            elif prices[i] > prices[j] and t == 0:
                t += 1
                break
        answer.append(t)
    answer.append(0)
    return answer
    # # 0) 정확성 6.7, 효율성 0.0, 6.7/100(30분)
    # for i in range(len(prices)):
    #     t = 0
    #     for j in range(i+1, len(prices)):
    #         if i == len(prices) - 1:
    #             break
    #         if prices[i] <= prices[j]:
    #             t += 1
    #         elif prices[i] > prices[j] and t == 0:
    #             t += 1
    #             break
    #     answer.append(t)