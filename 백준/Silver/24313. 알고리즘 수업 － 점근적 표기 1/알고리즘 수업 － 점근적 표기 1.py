a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

# 판별식 f(n) <= c*g(n)
# (a1-c)*n0 + a0 <= 0
# a1-c > 0 인 경우 성립하지 않으므로 조건 추가
if a1*n0 + a0 <= c*n0 and a1-c <= 0:
    print(1)
else:
    print(0)