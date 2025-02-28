def solution(s):
    s = s.strip("{").strip("}")
    s = s.split("},{")
    s = [v.split(",") for v in s]
    s.sort(key = lambda x : len(x))
    
    answer = []
    
    for v in s:
        for e in v:
            if int(e) not in answer:
                answer.append(int(e))
            
    return answer