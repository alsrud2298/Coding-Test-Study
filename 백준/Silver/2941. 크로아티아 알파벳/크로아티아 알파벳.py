croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

S = input()
count = 0
for x in croatia:
    if x in S:
        count += S.count(x)
        S = S.replace(x," ")
        
print(count+len(S.replace(" ","")))