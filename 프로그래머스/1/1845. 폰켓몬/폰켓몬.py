def solution(nums):
    target = len(nums) / 2
    u_num = len(set(nums))
    
    if u_num < target:
        answer = u_num
    else:
        answer = target
    return answer