import sys

N,X = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))

answer = [num for num in num_list if num < X]

for a in answer:
    print(a, end=" ")