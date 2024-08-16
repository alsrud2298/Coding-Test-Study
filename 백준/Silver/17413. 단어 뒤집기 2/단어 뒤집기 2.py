str = input()

stack = []
ans = ''
check = False # 괄호안의 여부 체크

for s in str:
    if s == '<':
        check = True # 괄호 안이라면
        for _ in range(len(stack)): # < 이전의 단어는 뒤집어서 ans에 추가
            ans += stack.pop()

    stack.append(s)

    if s == '>':
        check = False # 괄호 빠져나옴
        for _ in range(len(stack)): 
            ans += stack.pop(0) # 괄호 안의 값은 앞에서부터 추가

    if s == ' ' and check == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop() # 들어간 공백 빼주기 
                continue
            ans += stack.pop()
        ans += ' ' # 마지막에 다시 공백 넣기

if stack: # 스택에 값이 남아있는 경우
    for _ in range(len(stack)):
        ans += stack.pop()

print(ans)