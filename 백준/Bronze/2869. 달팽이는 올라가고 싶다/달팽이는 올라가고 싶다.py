A,B,V = map(int,input().split())
day = 0
day = (V-A)/(A-B)+1
print(int(day) if day == int(day) else int(day)+1)