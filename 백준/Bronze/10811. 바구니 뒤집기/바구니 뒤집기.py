#1번부터 N번까지 바구니
#입력 범위 내 바구니 역순으로 바꾸기 M번

N,M = map(int,input().split())

basket = [i for i in range(1,N+1)]

for i in range(M):
    s,e = map(int,input().split())
    temp = reversed(basket[s-1:e])
    basket[s-1:e] = temp

for b in basket:
    print(b,end=" ")
    