def solution(quiz):

    bf_eq = [q.split('=')[0].strip() for q in quiz]
    af_eq = [q.split('=')[1].strip() for q in quiz]
    
    bf_answer = [eval(b) for b in bf_eq]
    
    result = []
    for i in range(len(quiz)):
        if bf_answer[i] == int(af_eq[i]):
            result.append("O")
        else:
            result.append("X")
    return result