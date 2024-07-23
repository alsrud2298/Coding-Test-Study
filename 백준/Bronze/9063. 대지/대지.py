# 점을 모두 포함하는 가장 작은 직사각형의 넓이
# x,y 최대 - 최소 값?

N = int(input())
x_list = []
y_list = []

for i in range(N):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

result_x = max(x_list) - min(x_list)
result_y = max(y_list) - min(y_list)

print(result_x * result_y)
    