n = int(input())
target_num = 666
cnt = 0

while True:
    if '666' in str(target_num):
        cnt += 1
    
    if cnt == n:
        break
    
    target_num +=1

print(target_num)
    