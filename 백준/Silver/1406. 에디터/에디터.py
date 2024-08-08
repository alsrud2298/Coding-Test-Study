from sys import stdin

left = list(input())
right = []

for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'L' and left: # left가 비어있지 않으면
        right.append(left.pop())
    elif command[0] == 'D' and right: #right가 비어있지 않으면
        left.append(right.pop())
    elif command[0] == 'B' and left: # left가 비어있지 않으면
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]

print(''.join(answer))