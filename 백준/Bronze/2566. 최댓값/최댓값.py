max = 0
matrix = [[0]*9 for _ in range(9)]
row,col = 0,0
for i in range(9):
    matrix[i] = list(map(int,input().split()))
    for j in range(9):
        if max < matrix[i][j]:
            max = matrix[i][j]
            row = i
            col = j
print(max)
print(row+1,col+1)