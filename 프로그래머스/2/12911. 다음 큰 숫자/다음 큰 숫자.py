def solution(n):
    flag = True
    temp = n
    answer = 0
    bin1 = str(bin(n)).count("1")
    while flag:
        temp += 1
        bin2 = str(bin(temp)).count("1")
        if bin1 == bin2:
            answer = temp
            break
    return answer