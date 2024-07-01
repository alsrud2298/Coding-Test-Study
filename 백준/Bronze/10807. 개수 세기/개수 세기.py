import sys

n = int(sys.stdin.readline())
nums = map(int,sys.stdin.readline().split())
target = int(sys.stdin.readline())
cnt = 0
for i in nums:
    if i == target:
        cnt +=1
        
print(cnt)
        