# 직사각형이 되는 나머지 한 점 = x,y 중 하나만 있는 값들의 조합
x_list = []
y_list = []
result_x = 0
result_y = 0

for i in range(3):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

for x in x_list:
    if x_list.count(x) == 1:
        result_x = x
        
for y in y_list:
    if y_list.count(y) == 1:
        result_y = y
        
print(result_x, result_y)