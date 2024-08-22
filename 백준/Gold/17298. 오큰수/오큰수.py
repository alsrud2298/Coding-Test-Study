N = int(input())
seq = list(map(int, input().split()))
NGE = [-1]*N
stack = [0] # 0번 인덱스

for i in range(1,N):
    # 오른쪽부터 탐색 - stack[-1]
    # seq[i]의 오른쪽에 있으면서 & seq[i]보다 큰 수 중 가장 왼쪽 값
    while stack and seq[stack[-1]] < seq[i]:
        NGE[stack.pop()] = seq[i] # 해당 인덱스 칸은 seq[i]
    stack.append(i) # 다음 NGE[i] 구하기

print(*NGE)