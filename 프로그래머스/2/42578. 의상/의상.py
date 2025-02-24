def solution(clothes):
    dict = {}
    for item,type in clothes:
        if type in dict:
            dict[type] += 1
        else:
            dict[type] = 1
    
    answer = 1
    
    for _, value in dict.items():
        answer *= (value + 1)
    
    return answer - 1