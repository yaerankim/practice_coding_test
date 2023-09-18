from collections import deque

# 아직 해결X
def solution(bridge_length, weight, truck_weights):
    answer = 0
    d = deque(truck_weights)
    b_truck, b_weight = 0, 0
    for _ in range(len(truck_weights)):
        if b_truck <= bridge_length and b_weight <= weight:
            b_truck += 1
            b_weight += d.popleft()
        else:
            answer += (bridge_length + 1)
            b_truck, b_weight = 0, 0
            break
    return answer