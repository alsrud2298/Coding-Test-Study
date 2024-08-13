# deeue 활용
from collections import deque

q = deque()
n,k = map(int,input().split())
answer = []
for i in range(1,n+1): q.append(i)

while q:
    for _ in range(k-1):
        q.append(q.popleft())
        
    answer.append(q.popleft())

print(str(answer).replace('[','<').replace(']','>'))