
# n = int(input('Enter the number:'))

# count = 0
# for i in range(1,n+1):

#     if n%i == 0:
#         count += 1
    
# if count >= 2:
#     print('The number is not a Prime Number') 
# else:
#     print("It is a Prime Number")



# Optimized one : Here the factors of n are only found till n//2 only..from (2 to n)

# n = int(input('Enter the number:'))

# count = 0
# for i in range(2,n//2 + 1):

#     if n%i == 0:
#         count += 1
#         break
    
# if count == 0:
#     print(f'The number {n} is  a Prime Number') 
# else:
#     print("It is a not Prime Number")





# Prime number from 1 to N , time-complexity in O(N**2)


# n = int(input('Enter the number:'))

# for val in range(2,n+1):
#     count = 0
#     for i in range(2 , val//2 + 1):

#         if val%i == 0:
#             count += 1
#             break
        
#     if count == 0:
#         print(val, end=" ") 



# N prime numbers so for n = 5 here is the output ( 2, 3, 5, 7 , 11)

# n = int(input('Enter the no of prime :'))
# prime_no_count = 0
# val = 2
# while prime_no_count < n:

#     count = 0
#     for i in range(2, val//2 + 1):

#         if val % i == 0:
#             count += 1
#             break

#     if count == 0:

#         print(val , end = " ")
#         prime_no_count += 1

#         # if prime_no_count == n:
#         #     break

#     val +=1



   