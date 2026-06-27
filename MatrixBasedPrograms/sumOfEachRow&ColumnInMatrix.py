row = int(input('Enter to no of rows: '))
col  = int(input('Enter the no of col : '))

matrix1 = [[int(input('Enter the values : '))  for col in range(col)] for row in range(row) ]

print("Matrix 1 ")

for i in range(row):
    for j in range(col):

        if matrix1[i][j] < 10:

            print('0' + str(matrix1[i][j]), end = " ")
        else:
            print(matrix1[i][j], end = ' ')

    print()



srow = []
scol = []


for i in range(row):
    res1 = 0
    res2 = 0


    for j in range(col):
        res1 += matrix1[i][j]
        res2 += matrix1[j][i]


    srow += [res1]
    scol += [res2]

print('Row sum: ', srow)
print('Col Sum: ', scol)

        