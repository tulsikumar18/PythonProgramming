#product of 1 to N
# This is a Factorial Problem..

# n = int(input('Enter the number: '))

# res = 1

# for i in range(1,n+1):

#     res *= i
# print(res)


# sum of first n even number ::: n(n+1)

# n = int(input('Enter the number: '))

# res = 0

# res = n * (n+1)
# print("Even Sum: ", res)



# # sum of first n Odd number ::: n**2

# n = int(input('Enter the number: '))

# res = 0

# res = n **2
# print("Odd Sum: ", res)


# Now for sum of Even number till 10
#30
# n = int(input('Enter the number: '))
# res = 0

# for i in range(1,n+1):

#     if i%2 == 0:
#         res += i
# print(res)



# Factors of N

# n = int(input('Enter the number: '))

# for i in range(1,n+1):

#     if n % i == 0:
#         print(i , end=" ")




# Using the List Comprehension..Find the Factors..

# n = int(input('Enter the number: '))

# # this will return a List..
# print([x for x in range(1,n+1) if n%x == 0])

# # Peform unpacking for that..

# print(*[x for x in range(1,n+1) if n%x == 0])



# Using the List Comprehension..Find the Count of  Factors..use len() function for the List

# n = int(input('Enter the number: '))

# this will return a List..
# print(len([x for x in range(1,n+1) if n%x == 0]))



# count the factors to verify if it is Prime Number..

n = int(input('Enter the number: '))
count = 0

for i in range(1,n+1):

    if n % i == 0:
        count += 1

if count == 2:
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')
