N = int(input())

for _ in range(N):
    stack = []
    str = input()
    for s in str:
        if s == "(": # "("괄호가 나오면 stack에 넣는다
            stack.append(s)
        elif s == ")": # ")"괄호가 나오면
            if stack: # 스택이 비어있지 않으면
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack: # 스택이 비어있지 않으면
            print("NO")
        else:
            print("YES")