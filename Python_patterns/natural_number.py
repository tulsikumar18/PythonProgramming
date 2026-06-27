
# n = int(input('n:'))


# for i in range(1, n+1):

#     print(i , end = " ")




# n odd numbers.. we have to iterate till 2n+1 to get the value..


# n = int(input("n:"))

# for i in range(1, 2 * n + 1):

#     if i%2 != 0:

#         print(i, end = " ")


# n even numberss..


# n = int(input("n:"))

# for i in range(2, 2 * n + 1):

#     if i%2 == 0:

#         print(i, end = " ")



# OR

# n = int(input("n:"))

# for i in range(2, 2 * n + 1,2):   # start the i from 1 and use formula 2*i

#     print(i, end = " ")



# square of numbers


# n = int(input("n:"))

# for i in range(1, n+1):

#     print(i ** 2, end = " ")


# cube number series..

# n = int(input("n:"))

# for i in range(1, n+1):

#     print(i ** 3, end = " ")


#Patterns..
# 2 1 4 3 6 5 8 % 

# n = int(input("n:"))

# for i in range(n):

#     if i%2 == 0:

#         print(i+2, end = " ")
#     else:
#         print(i, end = " ")


# fibonacci series..

# 0 , 1 , 1, 2, 3, 5, 8, 13

n = int(input('n:'))

a, b = 0,1

for i in range(n):

    print (a, end = " ")

    # c = a+b
    # a=b
    # b=c
    
    a,b = b,a+b


    
