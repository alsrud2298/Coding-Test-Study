
# n 입력
n = int(input())

# 생성자 찾기
for i in range(1, n+1):
    num = sum((map(int, str(i)))) # i의 각 자리수를 더함
    num_sum = i + num # 분해합
    # i가 작은 수부터 차례로 들어가므로 처음 분해합과 같아질때가 가장 작은 생성자임
    if num_sum == n:
        print(i)
        break
    if i == n: # 생성자 = 입력값 -> n까지 다 돌아도 생성자가 없다는 뜻
        print(0)
        