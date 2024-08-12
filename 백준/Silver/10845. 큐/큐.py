# 10845 큐
import sys
# Queue - FIFO
n = int(sys.stdin.readline().strip())
stack = []

for i in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 'pop':
        if stack:
            print(stack.pop(0))
        else:
            print(-1)