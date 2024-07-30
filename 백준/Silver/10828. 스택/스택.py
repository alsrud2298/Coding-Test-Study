# 리스트로 스택 구현 
# n 입력
import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
        stack.append(int(order[1]))
        
    elif order[0] == 'pop':
        if not stack: # 스택이 비어있으면
            print(-1)
        else:
            print(stack.pop()) # 마지막 원소 리턴 후 삭제
  
    elif order[0] == 'size':
        print(len(stack))
    
    elif order[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    
    elif order[0] =='top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            