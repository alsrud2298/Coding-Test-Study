def solution(n):
    # n까지 뛰는 방법을 차례대로 저장하기 위한 배열 선언
    # n=1인 경우, dp[1]에서 에러가 날 것이므로 필요한 배열보다 1칸 더 선언
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 2
    
    # dp를 차례대로 채워 넣는다.
    for i in range(2,n):
        dp[i] = dp[i-2] + dp[i-1]
        
    return dp[n-1] % 1234567