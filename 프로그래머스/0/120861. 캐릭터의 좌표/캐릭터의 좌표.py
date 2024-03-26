def solution(keyinput, board):
    direction_list = ['up','down','left','right']
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    w,h = (board[0]-1)/2, (board[1]-1)/2
    y,x = 0,0
    for key in keyinput:
        for i in range(4):
            if key == direction_list[i]:
                ny,nx = y+dy[i], x+dx[i]
                if -w <= ny <= w and -h <= nx <= h :
                    y,x = ny,nx
                else:
                    pass
    return [y,x]