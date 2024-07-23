angle = []

for i in range(3):
    ang = int(input())
    angle.append(ang)

sum_ang = sum(angle)

if sum_ang != 180:
    print('Error')
elif angle.count(60) == 3:
    print('Equilateral')
elif angle.count(angle[0])==2 or angle.count(angle[1]) == 2:
    print('Isosceles')
elif angle.count(angle[0]) == 1 and angle.count(angle[1]) == 1:
    print('Scalene')
    