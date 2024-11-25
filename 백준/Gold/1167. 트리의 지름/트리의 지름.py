import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
# 그래프 정보
graph = [[] for _ in range(n+1)]

for _ in range(n):
    tree = list(map(int,input().split())) # [1,3,2,-1]
    # 정점 번호를 그래프의 인덱스로 사용
    # 홀수 = 연결된 정점 번호, 짝수 = 거리
    for i in range(1, len(tree)//2):
        # 정점 번호, 거리 저장
        graph[tree[0]].append((tree[2*i-1], tree[2*i]))
# 방문 배열
visited = [-1] * (n+1)
visited[1] = 0 # 로트 노드 거리는 0으로 초기화
    
# dfs 함수
def dfs(x, distance):
    for i,w in graph[x]:
        # 아직 방문하지 않은 노드이면 현재까지의 거리 + 해당 노드까지의 가중치로 방문 배열 값 변경
        if visited[i] == -1:
            visited[i] = distance + w
            dfs(i, distance + w)
dfs(1,0) # 루트 노드에서 각 정점까지의 거리 계산
max_distance = max(visited)
max_node = visited.index(max_distance)

# max_node에서 시작해 각 정점까지의 거리 계산
visited = [-1] * (n+1) # 거리 배열 초기화
visited[max_node] = 0
dfs(max_node,0)
# 트리의 지름
print(max(visited))