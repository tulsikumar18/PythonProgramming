n = int(input('Enter the number : '))

# temp = n

# rev = 0
# while  n != 0:
#     rem = n % 10

#     rev = rev * 10 + rem

#     n //= 10

# if rev == temp:
#     print('Palindrome')
# else: 
#     print('Not Palindrome')



if str(n) == str(n)[: : -1]:
    print('Palindrome')
else:
    print('Not a Palindrome')
    
