# 짝수라인 : 분모가 1씩 늘어나고, 분자가 1씩 줄어듦
# 홀수라인 : 분모가 1씩 줄어들고, 분자가 1씩 늘어남

# 1. 입력받은 x를 1씩 늘려가면서 라인 수에서 빼서 몇번째 줄, 몇번째 숫자인지 구한다
# 2. 짝수번째 줄인지, 홀수번째 줄인지에 따라 확인

num = int(input())

line = 1
while num > line:
    num -= line
    line += 1

# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')