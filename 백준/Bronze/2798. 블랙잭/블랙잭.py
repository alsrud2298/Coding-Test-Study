# N,M 입력
N,M = map(int,input().split())

# N장의 카드 입력
cards = list(map(int,input().split()))

# 정답 저장 변수 선언
ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            check = cards[i] + cards[j] + cards[k]
            if check > ans and check <= M:
                ans = check
print(ans)