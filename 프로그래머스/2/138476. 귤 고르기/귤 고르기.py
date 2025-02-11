def solution(k, tangerine):
    t_dict = {}
    result = 0
    
    for num in tangerine:
        if num in t_dict:
            t_dict[num] += 1
        else:
            t_dict[num] = 1
    sorted_dict = sorted(t_dict.items(), reverse = True, key = lambda x:x[1])
    
    for item in sorted_dict:
        if item[1] >= k:
            return result + 1
        else:
            k -= item[1]
            result += 1
