# 소수의 개수 출력
# 소수 : 1과 자기 자신만을 약수로 가지는 수

N = int(input())
prime = []

numbers = list(map(int,input().split()))

for i in numbers:
    factors = []
    for j in range(1,i+1):
        if i % j == 0: # 약수 구하기
            factors.append(i)
    if len(factors) == 2: # 약수가 1과 자기자신 2개만 있는 경우
        prime.append(i) # 소수

print(len(prime))
        