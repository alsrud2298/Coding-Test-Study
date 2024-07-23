while True:
    a,b,c = map(int,input().split())
    
    tri_list = sorted([a,b,c]) # 삼각형 조건 판별을 위해 오름차순 정렬

    if a==b and b==c and c==0: # 종료 조건
        break
    if tri_list[-1] >= tri_list[0] + tri_list[1]:
        print("Invalid")
    elif tri_list.count(a) == 3:
        print("Equilateral")
    elif tri_list.count(a) == 2 or tri_list.count(b) == 2:
        print("Isosceles")
    elif tri_list.count(a) == 1 or tri_list.count(b) == 1:
        print("Scalene")