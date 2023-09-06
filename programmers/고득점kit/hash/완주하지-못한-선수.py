from collections import Counter

def solution(participant, completion):
    answer = ''
    _hash = {}
    key = list(set(participant))
    p_list = Counter(participant)
    c_list = Counter(completion)
    for i in range(len(p_list)):
        if p_list[key[i]] != c_list[key[i]]:
            answer = key[i]
            break          
    return answer
