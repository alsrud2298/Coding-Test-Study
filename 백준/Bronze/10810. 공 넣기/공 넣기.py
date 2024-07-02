import sys
N,M = map(int,sys.stdin.readline().split())
basket = [0]*N

for i in range(M):
    start,end,ball = map(int,sys.stdin.readline().split())
    for j in range(start,end+1):
        basket[j-1] = ball

for b in basket:
    print(b,end=' ')
    
    
    