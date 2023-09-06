import math

def solution(clothes):
    clothes_dict = {}
    for v, k in clothes:
        clothes_dict.setdefault(k,[])
        clothes_dict[k].append(v)
        
    value_cnt = list(map(len, clothes_dict.values()))
    value_cnt = [v+1 for v in value_cnt]
    
    answer = math.prod(value_cnt) - 1
    return answer
