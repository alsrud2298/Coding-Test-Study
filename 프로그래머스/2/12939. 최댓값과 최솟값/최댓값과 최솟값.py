def solution(s):
    num = s.split(" ")
    max_n =  int(num[0])
    min_n = int(num[0])
    for n in num:
        n = int(n)
        if n > max_n: # 0 1 2 3 4
            max_n = n # 0 1
        if n < min_n:
            min_n = n
    answer = str(min_n) + " " + str(max_n)
    return answer