# 1,3,5,7,9,7,5,3,1
N = int(input())
cnt = 1
rows = 2*N-1

for i in range(1,2*N):
    blank = int((rows - cnt)/2)
    print(' '*blank+'*'*cnt)
    if i < N:
        cnt += 2
    else:
        cnt -= 2