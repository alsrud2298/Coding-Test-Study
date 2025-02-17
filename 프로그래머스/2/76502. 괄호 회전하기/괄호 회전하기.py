def solution(s):
    # 올바른 괄호 문자열인지 확인
    def is_valid_paren(paren_string):
        stack = []
        matching = {')':'(',']':'[','}':'{'} # 닫는 괄호에 대한 짝이 되는 여는 괄호 매핑
        for char in paren_string:
            if char in matching.values(): # 여는 괄호라면 스택에 추가
                stack.append(char)
            elif char in matching.keys(): # 닫는 괄호라면 스택에서 마지막 여는 괄호와 짝을 맞추고
                if stack and stack[-1] == matching[char]: # 짝이 맞으면
                    stack.pop() # 스택에서 제거
                else:
                    return False # 맞지 않으면 올바른 괄호 문자열이 아님
        return len(stack) == 0 # 성공적으로 스택을 비웠으면 모든 괄호가 짝이 맞는 것
    count = 0
    for i in range(len(s)):
        rotated_s = s[i:] + s[:i] # 슬라이싱으로 회전
        if is_valid_paren(rotated_s):
            count += 1
    return count