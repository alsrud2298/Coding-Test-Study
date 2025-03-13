# 최단거리, 동일 비용 = bfs 로 구현
from collections import deque

def solution(maps):
    queue = deque([(0,0)])
    n,m = len(maps), len(maps[0])
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
        
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
                
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1
