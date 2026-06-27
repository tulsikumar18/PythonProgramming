
# A number is said to be perfect number when all factors sum except that number is equal to that number

# all factors sum ~ {n} = n
# Factors are always available till n / 2 only

# n = int(input('Enter the number:'))

# res = 0

# for i in range(1 , n//2 + 1):

#     if n % i == 0:
#         res += i
    
# if res == n:
#     print(f'{n} is a perfect number ')




# # perfect number between 1 to N 


# n = int(input('Enter the range of n:'))

# for j in range(1 , n+1):

#     res = 0

#     for i in range(1 , j//2 + 1):

#         if j % i == 0:
#             res += i
        
#     if res == j:
#         print(j , end = " ")






# N perfect Number 


n = int(input('Enter the no of perfect no :'))

val = 1
count = 0
while True:

    res = 0

    for i in range(1 , val //2 + 1):

        if val % i == 0:
            res += i
        
    if res == val:
        print(val , end = " ")
        count += 1

        if count == n:
            break

    val += 1
