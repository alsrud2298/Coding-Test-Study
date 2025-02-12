def solution(n,a,b):
	round = 0 # 초기값 설정
	while a != b:
		round += 1
		# 1~8이 있을 때, 1을 더하고 2로 나눈 몫이 11223344 이런식으로 됨
		a = (a+1) // 2
		b = (b+1) // 2
	return round