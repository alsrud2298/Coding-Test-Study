formula = list(input())
stack = []
answer = ''

for s in formula:
    if s.isalpha(): #피연산자는 바로 정답 문자열에 추가
        answer += s
    elif s == '(': # 여는 괄호는 무조건 스택에 추가
        stack.append(s)
    elif s == '*' or s == '/': # 곱셉 나눗셈은
        # 스택에 존재하는 *이나 /를 pop하여 결과값에 저장
        while stack and (stack[-1] == '*' or stack[-1]=='/'): 
            answer += stack.pop() 
        stack.append(s)
    elif s == '+' or s == '-': # 덧셈/뺄셈은
        # 여는 괄호 이전에 존재하는 값들을 모두 pop해 결과에 저장
        while stack and stack[-1] != '(': 
            answer += stack.pop()
        stack.append(s) # stack에 추가
    elif s == ')': # 닫는 괄호는
        # 여는 괄호 직전 까지의 값 모두 pop해 결과값에 저장하고
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop() # '('를 빼는 작업
        
while stack: # 남아 있는 문자 정답으로 추가
    answer += stack.pop()
   
print(answer)              