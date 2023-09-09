def solution(prices):
    answer = []
    # 0) 정확성 6.7, 효율성 0.0, 6.7/100(30분)
    for i in range(len(prices)):
        t = 0
        for j in range(i+1, len(prices)):
            if i == len(prices) - 1:
                break
            if prices[i] <= prices[j]:
                t += 1
            elif prices[i] > prices[j] and t == 0:
                t += 1
                break
        answer.append(t)
    return answer