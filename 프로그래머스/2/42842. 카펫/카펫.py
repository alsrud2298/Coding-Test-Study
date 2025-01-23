def solution(brown, yellow):
    w,h = 0,0
    for i in range(1,yellow + 1):
        if yellow % i == 0:
            y_h = i
            y_w = yellow // i
            if 2*y_w + 2*y_h + 4 == brown:
                w,h = y_w + 2, y_h + 2
                break
    if w >= h:
        return [w,h]
    else:
        return [h,w]