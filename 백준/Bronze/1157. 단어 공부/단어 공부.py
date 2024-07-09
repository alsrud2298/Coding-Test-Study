S = input().upper()
alpha_list = [s for s in S] # 알파벳 리스트로 저장
dict = {} # 개수 세기용 딕셔너리 생성
for a in alpha_list:
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1
value_list = list(dict.values()) # 개수 리스트 
if value_list.count(max(value_list)) > 1: # 가장 많이 사용된 알파벳이 여러개 존재하는 경우
    print('?')
else:
    for k in dict.keys(): # 가장 많이 사용된 알파벳 출력
        if dict[k] == max(value_list):
            print(k)