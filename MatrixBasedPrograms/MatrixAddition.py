
## Write the program to take input in the form of user input and display in the form of matrix..
## also perform matrix addition..



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



matrix2 = [[int(input('Enter the values : '))  for col in range(col)] for row in range(row) ]

print("Matrix 2 ")

for i in range(row):
    for j in range(col):

        if matrix2[i][j] < 10:

            print('0' + str(matrix2[i][j]), end = " ")
        else:
            print(matrix2[i][j], end = ' ')

    print()


## Result.. matrix..

result = [[ 0 for col in range(col)] for row in range(row) ]

print("Result.. ")

for i in range(row):
    for j in range(col):

        result[i][j] = matrix1[i][j] + matrix2[i][j]



print("Result..  ")

for i in range(row):
    for j in range(col):

        if result[i][j] < 10:

            print('0' + str(result[i][j]), end = " ")
        else:
            print(result[i][j], end = ' ')

        
    print()
