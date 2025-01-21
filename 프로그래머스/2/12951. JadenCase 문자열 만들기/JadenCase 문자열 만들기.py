def solution(s):
    answer = []
    for word in s.split(" "):
        if word == "":
            word = ""
        elif word[0].isalpha():
            word = word[0].upper() + word[1:].lower()     
        else:
            word = word.lower()
        answer.append(word)
    return " ".join(answer)