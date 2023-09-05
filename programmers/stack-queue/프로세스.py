from collections import deque # , OrderedDict

def solution(priorities, location):
    # 0) 다른 사람 코드(참고: https://velog.io/@naro-kim/%EC%8A%A4%ED%83%9D%ED%81%90-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
    q = deque(priorities)
    answer = 0
    while q:
        m = max(q)
        l = q.popleft()
        location -= 1 
        if l != m:
            q.append(l) # 우선순위 더 높은게 있으면 뒤로 삽입
            if location < 0: # 구하고자 하는 프로세스가 맨 뒤로 가게 되면
                location = len(q) -1
        else:
            answer += 1 # 실행하게 되면
            if location < 0:
                break

    return answer
    # 1) 다른 사람의 코드에서 deque 힌트 얻어 적용해보기. 실패. 30분 소요.
#     deq = deque()
#     for i in range(len(priorities)):
#         deq.append((i, priorities[i])) # deq에 dict 형식으로 데이터 넣어 옮기기
        
#     deq2 = deque()
#     first = priorities[0]
#     deq2.append((0, first)) # 맨 앞은 무조건 추가
#     stack_on = False # stack으로 전환되면 True, 계속 queue면 False
#     index = 0 # 가장 높은 중요도의 index
#     while True:
#         if len(deq) == 0:
#             break
#         if stack_on == False and first >= deq[0][1]: # queue
#             deq2.append(deq.popleft())
#             continue
#         if first < priorities[0]: # stack
#             deq2.appendleft(deq.popleft())
#             stack_on = True
#             continue
#             # stack으로 한 번 잠깐 바뀐 경우에는 조금 다른 형태의 queue 사용
#         if stack_on == True and first >= deq[0][1]:
#             deq2.insert(index + 1, deq.popleft())
#             continue
#         if stack_on == True and first < deq[0][1]: # 또 중요도 높은게 나타나면
#             deq2.insert(index + 1, deq.popleft())
#             continue
#     print(deq2)
       
    # 2) 내가 푼 방식. 실패. 40분 소요.
#     # p_dict = {}
#     # # 각 문서들의 index 번호 지정해둠
#     # # 같은 중요도 가진 문서들도 있기 때문에 구별 위해 index 필요
#     # for i in range(len(priorities)):
#     #     p_dict[i] = priorities[i]
        
#     order = []
#     order_dict = OrderedDict()
#     # first = priorities.pop(0) # 이러면 삭제되니까 [0] 사용하기
#     first = priorities[0]
#     order.append(first) # 맨 앞은 무조건 추가
#     stack_on = False # stack으로 전환되면 True, 계속 queue면 False
#     index = 0 # 가장 높은 중요도의 index
#     count = 0 # dict key용
#     while True:
#         order_dict[count] = priorities.pop(0)
#         if len(priorities) == 0:
#             break
#         if stack_on == False and first >= priorities[0]: # queue
#             order.append(order_dict[count])
#             count += 1
#             continue
#         if first < priorities[0]: # stack
#             order.insert(0, order_dict[count])
#             count += 1
#             stack_on = True
#             continue
#             # stack으로 한 번 잠깐 바뀐 경우에는 조금 다른 형태의 queue 사용
#         if stack_on == True and first >= priorities[0]:
#             order.insert(index + 1, order_dict[count])
#             count += 1
#             continue
#         if stack_on == True and first < priorities[0]: # 또 중요도 높은게 나타나면
#             order.insert(index + 1, order_dict[count])
#             count += 1
#             continue
#     print(order)
#     print(order_dict)
#     # return answer