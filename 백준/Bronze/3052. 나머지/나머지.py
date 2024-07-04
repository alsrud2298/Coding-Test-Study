# 42로 나눈 나머지 -> unique() 개수 출력

num_list = []
for i in range(10):
    num_list.append(int(input())%42)

print(len(set(num_list)))