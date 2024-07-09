# 전공 평점 = SUM(학점 * 과목 평점) / 학점 총 합
# P는 계산에서 제외
score = 0
total = 0 
for i in range(20):
    N,S,G = input().split()
    total += int(S.replace('.0',""))
    S = float(S)
    if G == 'A+':
        score += 4.5 * S
    elif G == 'A0':
        score += 4.0 * S
    elif G == 'B+':
        score += 3.5 * S
    elif G == 'B0':
        score += 3.0 * S
    elif G == 'C+':
        score += 2.5 * S        
    elif G == 'C0':
        score += 2.0 * S
    elif G == 'D+':
        score += 1.5 * S
    elif G == 'D0':
        score += 1.0 * S
    elif G == 'F':
        score += 0.0 * S
    elif G == 'P':
        total -= S
        
print(score/total)