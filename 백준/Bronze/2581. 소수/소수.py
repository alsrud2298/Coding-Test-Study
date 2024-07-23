# M이상, N이하 자연수 중 소수들의 합 & 소수 중 최솟값
M = int(input())
N = int(input())
prime = []
for num in range(M,N+1):
    no_prime = 0
    if num > 1 :
        for i in range(2,num):
            if num % i == 0:
                no_prime += 1 # 소수가 아닌 경우
                break
        if no_prime == 0: # 소수인 경우
            prime.append(num)
                
if len(prime) == 0 :
    print(-1)
else:
    print(sum(prime))
    print(min(prime))