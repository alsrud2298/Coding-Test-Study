import sys
N = int(input())
A = list(map(int,sys.stdin.readline().split()))

stack = [] # 인덱스 저장
NGF = [-1] * N
# 수열 F(i) 생성
F = [0] * 1000001 # N<= 1,000,000
for x in A:
    F[x] += 1
 
for i in range(N):# A[i]보다 오른쪽에 있으면서
    while stack and F[A[stack[-1]]] < F[A[i]]: # F(Ai)보다 큰수 중 가장 왼쪽에 있는 수
        NGF[stack.pop()] = A[i]
    stack.append(i)
    
print(*NGF)