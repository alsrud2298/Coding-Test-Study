# 각 알파벳이 단어에 몇 개 포함되어 있는지?

word = input()

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
        'q','r','s','t','u','v','w','x','y','z']
answer = []

for a in alpha: # 알파벳 순으로 순회
    answer.append(word.count(a)) #개수 세기
    
print(*answer)