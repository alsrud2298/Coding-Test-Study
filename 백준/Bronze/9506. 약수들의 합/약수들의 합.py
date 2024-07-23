while True:
    # 입력 받기
    N = int(input())
    factors = []
    
    if N == -1: # -1이 주어진 경우 while문 탈출
        break

    for i in range(1,N+1): # 약수 구하기
        if N % i == 0:
            factors.append(i)

    if sum(factors[:-1]) == N: # 자신을 제외한 약수의 합 = N이면
        print(factors[-1],'= ', end = "")
        for i in factors[:-2]:
            print(i, end=" ")
            print('+ ', end="")
        print(factors[-2])
    else: # 완전수가 아닌 경우
        print(factors[-1], "is NOT perfect.")