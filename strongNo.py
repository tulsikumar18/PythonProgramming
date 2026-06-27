

# strong number -> sum of factorial of every digit is equal to n only 

# import math
# n = int(input('Enter the  n:'))

# val = n
# res = 0
# while val != 0:

#     rem = val % 10
#     res += math.factorial(rem)
#     val //= 10

# if res == n:

#     print(n, end=" ")



# strong number b/w 1 to N

# import math
# n = int(input('Enter the range n:'))


# for j in range(1, n+1):

#     val = j
#     res = 0
#     while j != 0:

#         rem = j % 10
#         res += math.factorial(rem)
#         j //= 10

#     if res == val:

#         print(res, end=" ")





# N strong number 


import math
n = int(input('Enter the no of n:'))

val = 1
count = 0
while True:
    temp = val
    res = 0
    while temp != 0:

        rem = temp % 10
        res += math.factorial(rem)
        temp //= 10

    if res == val:

        print(res, end=" ")
        count += 1
        if count == n:
            break
    val +=1