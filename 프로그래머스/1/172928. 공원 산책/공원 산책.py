def solution(park, routes):
    map = [[0]*(len(park[0])) for _ in range(len(park))]
    # 정보 입력
    for i in range(len(park)):
        for j in range(len(park[0])):
            map[i][j] = park[i][j]
            
    direction = [d[0] for d in routes]
    count = [int(d[2]) for d in routes]
    
    # 시작 위치 찾기
    start = [(i,j) for i in range(len(park)) for j in range(len(park[0])) if map[i][j] == 'S']
    x,y = start[0][0], start[0][1]

    # 방향 설정
    dir = ['N','S','W','E']
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    
    for d,c in zip(direction,count):
        tx,ty = x,y
        for _ in range(c):
            nx = x + dx[dir.index(d)]
            ny = y + dy[dir.index(d)]
            if 0 <= nx < len(park) and 0 <= ny < (len(park[0]))and map[nx][ny] != 'X':
                x,y = nx, ny
            else:
                x,y = tx,ty # 이전 위치로 돌아감
                break

    return [x,y]