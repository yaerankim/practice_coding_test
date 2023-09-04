def solution(nums):
    # 1) set() 사용할 경우
    # answer = 0
    # # 선택할 수 있는 폰켓몬 수
    # select_nums = int(len(nums)/2)
    # # 선택할 수 있는 폰켓몬 종류 중복 없이
    # set_nums = list(set(nums))
    # if len(set_nums) > select_nums:
    #     answer = select_nums
    # else:
    #     answer = len(set_nums)
    # return answer
    
    # 2) hash 사용할 경우
    answer = 0
    pocket_hash = {}
    temp_list = []
    for i in range(len(nums)):
        pocket_hash[i] = nums[i]
    for count in range(1, int(len(nums)/2) + 1):
        for _, v in pocket_hash.items():
            if v in temp_list:
                continue
            if len(temp_list) == count:
                break
            temp_list.append(v)
    answer = len(temp_list)
    return answer
