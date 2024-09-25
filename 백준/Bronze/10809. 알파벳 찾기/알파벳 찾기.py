# 알파벳이 포함된 경우, 처음 등장 위치 아니라면 -1 출력

word = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l',
        'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

answer = []

for a in alpha:
    answer.append(word.find(a))

print(*answer)