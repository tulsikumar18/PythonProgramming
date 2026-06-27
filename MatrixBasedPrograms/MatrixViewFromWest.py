
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


## Result.. matrix..

result = [[ 0 for col in range(col)] for row in range(row) ]

print("Result.. ")

for i in range(row):

     # First building fully visible
    result[i][0] = matrix1[i][0]

    # Maximum height seen from west
    max_height = matrix1[i][0]

    for j in range(1, col): ## first column building is fully visible , so no changes to that..

        if matrix1[i][j] > max_height:

            result[i][j] = (matrix1[i][j] - max_height)

            max_height = matrix1[i][j]

        else:
            result[i][j] = 0


## replace the value of first column with the first column value of the matrix 1 as it will 
# remain same : 

for i in range(row):

    result[i][0] = matrix1[i][0]


print("Result 1 ")

for i in range(row):
    for j in range(col):

        if result[i][j] < 10:

            print('0' + str(result[i][j]), end = " ")
        else:
            print(result[i][j], end = ' ')

    print()