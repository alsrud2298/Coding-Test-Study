A,B = map(int,input().split())
time = int(input()) + B

if time >= 60:
    H = time // 60
    M = time % 60
else:
    H = 0
    M = time
    
if A + H >= 24:
    print(A+H-24,M)
else:
    print(A+H,M)