N = int(input())
count = 0

paper = [[0 for i in range(100)] for _ in range(100)]

for i in range(N):
    x,y = map(int,input().split())
    for w in range(x-1,x+10-1):
        for h in range(y-1,y+10-1):
            paper[w][h] = 1
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            count+=1
print(count)