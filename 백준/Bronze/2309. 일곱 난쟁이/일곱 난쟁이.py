from itertools import combinations

data = []
for i in range(9):
    data.append(int(input()))

combi = list(combinations(data,7))

for c in combi:
    if sum(c) == 100:
        target = c

print(*sorted(target))