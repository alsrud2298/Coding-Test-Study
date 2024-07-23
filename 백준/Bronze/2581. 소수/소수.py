# M이상, N이하 자연수 중 소수들의 합 & 소수 중 최솟값
M = int(input())
N = int(input())
prime = []
for i in range(M,N+1):
    factors = []
    for j in range(1, i+1):
        if i % j == 0:
            factors.append(j)
    if len(factors) == 2:
        prime.append(i)

if len(prime) == 0 :
    print(-1)
else:
    print(sum(prime))
    print(min(prime))