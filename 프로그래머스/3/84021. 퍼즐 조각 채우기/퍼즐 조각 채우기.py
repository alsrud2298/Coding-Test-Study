from collections import deque
def search_puzzle(board, blocks, state):
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # game: 1, table 0(빈칸)일때 스킵
            if board[i][j] == state_list[state] or visited[i][j]: continue
            blocks.append(bfs(i,  j, board,visited, state))
    blocks.sort(key = lambda x: len(x), reverse = True)

state_list = [1, 0]
def solution(game_board, table):
    global N

    N = len(game_board)
    game_blocks, table_blocks = [], []

    # 1. 조각 찾기
    search_puzzle(game_board, game_blocks, 0)
    search_puzzle(table, table_blocks, 1)


    answer = 0

    for empty in game_blocks:
        flag = False
        # 2. 절대 위치 변경
        game_puzzle = cover_puzzle(empty)

        for table_block in table_blocks:
            # 이미 빈칸을 채웠음을 나타냄
            if flag == True:    break
            # 조각의 개수가 적은 경우 볼 필요가 없음
            if len(game_puzzle) > len(table_block):
                continue
            table_puzzle = cover_puzzle(table_block)
            
            for _ in range(4):
                # 3. 회전
                table_puzzle, cnt = rotate(table_puzzle)

                if table_puzzle == game_puzzle:
                    answer += cnt
                    table_blocks.remove(table_block)
                    flag = True
                    break
    return answer


# 각 조각을 넣는 이차원 배열
def cover_puzzle(puzzle):
    x = [i[0] for i in puzzle]
    y = [i[1] for i in puzzle]

    r = max(y) - min(y) + 1
    c = max(x) - min(x) + 1
    temp = [[0] * r for _ in range(c)]

    for i, j in puzzle:
        temp[i-min(x)][j-min(y)] = 1
    return temp

# 조각을 회전(시계 90)
def rotate(puzzle):
    cnt = 0
    r, c = len(puzzle), len(puzzle[0])
    temp = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if puzzle[i][j] == 1: cnt += 1
            temp[j][r-1-i] = puzzle[i][j]
    return temp, cnt

# 격자 내부인지 아닌지 확인
def is_board(x, y):
    return 0 <= x < N and 0 <= y < N

# 퍼즐 조각 찾기, state(board 0/ table 1)
def bfs(x, y, board,visited, state):
    # 좌, 우, 위, 아래
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque()
    q.append([x, y])
    puzzle = [[x, y]]

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 격자 내부 존재하지 않거나 방문한 경우
            if not is_board(nx, ny):
                continue
            if visited[nx][ny] == 1:
                continue
            # 빈 칸인 경우
            if board[nx][ny] == state:
                visited[nx][ny] = 1
                q.append([nx, ny])
                puzzle.append([nx,ny])

    return puzzle