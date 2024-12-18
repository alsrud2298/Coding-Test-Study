S = input()
answer = ""
lower = []
upper = []
for i in range(ord('A'),ord('Z')+1):
    upper.append(chr(i))
for i in range(ord('a'),ord('z')+1):
    lower.append(chr(i))
    
for i in range(len(S)):
    if S[i].islower():
        if ord(S[i]) + 13 < 26:
            answer += lower[lower.index(S[i])+13]
        else:
            answer += lower[lower.index(S[i])+13-26]
    elif S[i].isupper():
        if ord(S[i]) + 13 < 26:
            answer += upper[upper.index(S[i])+13]
        else:
            answer += upper[upper.index(S[i])+13-26]
    else:
        answer += S[i]

print(answer)