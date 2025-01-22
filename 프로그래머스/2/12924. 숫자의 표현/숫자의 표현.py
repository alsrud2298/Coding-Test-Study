def solution(n):
    answer = 1 # 자기 자신
    for i in range(1, n//2 + 1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:  # 합이 n이 되면
                answer += 1
                break
            elif sum > n: # n보다 커질 경우 바로 탈출
                break
    return answer