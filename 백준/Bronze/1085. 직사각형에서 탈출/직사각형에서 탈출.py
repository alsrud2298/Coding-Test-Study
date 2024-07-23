# w*h 직사각형
# 직사각형의 경계선까지의 최소값

x,y,w,h = map(int,input().split())
distance = []
distance.append(w-x)
distance.append(h-y)
distance.append(x)
distance.append(y)

print(min(distance))