# 가로 입력 -> 세로로 공백없이 출력하기
# 5줄, 1개~15개

S = [[" "]*15 for _ in range(5)]
for i in range(5):
      word = input()
      for j,w in enumerate(word):
        S[i][j] = w
for j in range(15):
    for i in range(5):
        if S[i][j] != " ":
            print(S[i][j], end="")