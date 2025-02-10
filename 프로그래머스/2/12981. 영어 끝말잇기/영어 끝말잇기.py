def solution(n, words):
    answer = []
    word_list = [words[0]] # 등장한 단어 저장
    i = 0
    bf_word = words[0]
    for af_word in words[1:]:
        i += 1
        if (bf_word[-1] == af_word[0]) & (af_word not in word_list):
            word_list.append(af_word)
            bf_word = af_word
        else:
            if (i+1)%n == 0:
                answer.append(n)
            else:
                answer.append((i+1)%n)
            answer.append(i//n + 1)
            break
    if not answer:
        answer = [0,0]
        
    return answer