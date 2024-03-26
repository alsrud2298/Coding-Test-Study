# 모든 경우의 수 찾기 DFS?
def solution(board):
    N = len(board)
    
    # 지뢰 위치 찾기
    for y, row in enumerate(board):
        for x, area in enumerate(row):
            
            if area == 1:
                # 지뢰 주변 8방향 검사
                for dy in [-1,0,1]:
                    for dx in [-1,0,1]:
                        ny = y + dy
                        nx = x + dx
                        
                        if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 1:
                            board[ny][nx] = -1
    safe_area = sum([area.count(0) for area in board])

    return safe_area