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


# max  = 0
# for i in range(row):
#     for j in range(col):

#         if matrix1[i][j] > max:
#             max = matrix1[i][j]


# print("Max Elem : " , max)


## Aproach 2 : using max() function ..

maxi = 0
for i in range(row):

    if max(matrix1[i]) > maxi:
        maxi = max(matrix1[i])

    

print(maxi)