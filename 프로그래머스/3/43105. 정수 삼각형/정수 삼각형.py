# 아래에서 위로 올라가기
def solution(triangle):
    floor = len(triangle) - 1
    
    while floor > 0:
        for i in range(floor):
            # 아래 두 값 중 큰 값을 더해줌
            triangle[floor-1][i] += max(triangle[floor][i], triangle[floor][i+1])
        floor -= 1
    return triangle[0][0]