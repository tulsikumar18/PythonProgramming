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



d1 = 0
d2 = 0

print('Diagonal of matrix 1 ')

for i in range(row):

    for j in range(col):

        if i == j:
            d1 += matrix1[i][j]
        
        if i + j ==  row - 1:     ## if we take elif here then the middle one is not included in 2nd one so 
                                 ## that value has to be considered in both d1 as well as d2...

            d2 += matrix1[i][j]


print('sum of diagonal ', d1)
print()

print('sum of diagonal ', d2)
print(abs(d1 - d2))