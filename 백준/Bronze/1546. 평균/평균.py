# 점수 중 최댓값 M, 모든 점수를 점수/M*100으로 수정
# 새로운 평균 출력
N = int(input())

score_list = list(map(int,input().split()))
max_score = max(score_list)
score_list = [score/max_score*100 for score in score_list]

print(sum(score_list)/N)