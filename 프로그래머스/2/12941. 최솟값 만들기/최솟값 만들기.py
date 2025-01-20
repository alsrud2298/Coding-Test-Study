# 제일 큰 수와 가장 작은 수를 곱하면 누적합이 최소가 됨
# A는 오름차순, B는 내림차순으로 정렬해서 곱하기 & 누적합

def solution(A,B):
    return sum( i * j for i,j in zip(sorted(A), sorted(B, reverse = True)))

