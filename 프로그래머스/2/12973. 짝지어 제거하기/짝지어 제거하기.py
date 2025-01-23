def solution(s):
    stack = []
    
    for i in range(len(s)):
        if not stack: # stack이 비어있으면 push
            stack.append(s[i])
        else: # stack이 비어있지 않으면
            if stack[-1] == s[i]: # top과 s[i] 같은지 확인
                stack.pop() # 같으면 pop
            else:
                stack.append(s[i]) # 다르면 push
    
    if stack: # 스택에 값이 남아있는 경우
        return 0
    else: # 스택이 비어있는 경우
        return 1