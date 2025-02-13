def solution(elements):
    answer = []
    # 길이가 1인 경우
    answer += set(elements)
    # 길이가 n인 경우
    answer.append(sum(elements))
    
    for i in range(2,len(elements)):
        temp = elements + elements[:i-1]
        for j in range(0,len(elements)):
            answer.append(sum(temp[j:i+j]))
    return len(set(answer))