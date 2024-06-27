import sys
n = int(sys.stdin.readline())
stack = []
answer = []
flag = 0
cur = 1

for i in range(n):
    num = int(sys.stdin.readline())
    while cur <= num: # 입력한 수 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur += 1
        # 입력한 수를 만나면 while문 탈출.
        # cur = num일때까지 while문으로 스택을 쌓는다.
    
    if stack[-1] == num: # stack의 Top이 입력한 값과 같다면
        stack.pop() # stack의 top을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break
        # stack의 top이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        # 스택은 무조건 오름차순으로 push되기 때문에 top이 num보다 크면
        # 원하는 순열을 만들 수 없다.
if flag == 0: # 순열을 만들 수 있는 경우
    for i in answer:
        print(i)