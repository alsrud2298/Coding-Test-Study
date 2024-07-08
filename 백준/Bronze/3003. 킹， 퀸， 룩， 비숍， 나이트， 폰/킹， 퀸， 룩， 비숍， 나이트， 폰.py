# 킹1 퀸1 룩2 비숍2 나이트2 폰8
chess = list(map(int,input().split()))
temp = [1,1,2,2,2,8]
result = [0]*6
for i,k in enumerate(temp):
    if chess[i] > k:
        result[i] = -(chess[i]-k)
    else:
        result[i] = k - chess[i]

for a in result:
    print(a, end=" ")
