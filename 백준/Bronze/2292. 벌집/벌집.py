N = int(input())
flag = True
count = 1
room = 0
N -= 1

while flag:
    room += 1
    if N > 0:
        N = N - count*6
        count += 1
    else:
        flag = False

print(room)