def solution(citations):
    answer = 0
    citations.sort(reverse=True) # 내림차순으로 정렬
    
    for i in range(len(citations)):
        if (citations[i] < i+1):
            return i
    return len(citations) # 인용 횟수가 모두 같은 경우