import collections

def solution(want, number, discount):
    want_dict = {}
    answer = 0
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        discount_10 = discount[i:i+10]
        discount_dict = {}
        for j in discount_10:
            if j in discount_dict:
                discount_dict[j] += 1
            else:
                discount_dict[j] = 1
        if want_dict == discount_dict:
            answer += 1
    return answer

