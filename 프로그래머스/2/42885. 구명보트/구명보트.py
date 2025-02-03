def solution(people, limit):
    left = 0
    right = len(people) - 1
    answer = 0
    
    people.sort(reverse = True) # 오름차순 정렬
    
    while left <= right:
        if people[left] + people[right] <= limit:
            right -= 1 # 아니라면 무거운 쪽만 보내는 것이 더 이득
        left += 1
        answer += 1
    return answer