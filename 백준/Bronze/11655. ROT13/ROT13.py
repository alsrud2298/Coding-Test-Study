S = input()
answer = ""
    
for i in S:
    if i.islower():
        if ord('a') <= ord(i) + 13 <= ord('z'):
            answer += chr(ord(i) + 13)
        else:
            answer += chr(ord(i) - 13)
    elif i.isupper():
        if ord('A') <= ord(i) + 13 <= ord('Z'):
            answer += chr(ord(i) + 13)
        else:
            answer += chr(ord(i) - 13)

    else:
            answer += i

print(answer)