# N 최대 10,000,000 -> 시초 고려하기
# 굳이 소수 구할 필요없음. 나눠지는 가장 작은 수 찾기
N = int(input())
i = 2

while N != 1:
    if N%i == 0:
        print(i)
        N = N/i
    else:
        i += 1