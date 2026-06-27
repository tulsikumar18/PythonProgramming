#Armstrong Number is n = 123 then if (1 ** len(n) + 2 ** len(n) + 3 ** len(3))  = 123 then here
# N is Armstrong number..


# n = int(input('Enter the number:'))


# res = 0

# val = str(n)
# l = len(val)

# for i in range(l):

#     res += int(val[i]) ** l

# if res == n :
#     print(n , end = " ")



# # Armstrong number in the range of 1 to N 

# n = int(input('Enter the n : '))

# # J is used to control the values and i is used on string to access each string integer values 
# for j in range(1,n+1):

#     res = 0

#     val = str(j)
#     l = len(val)

#     for i in range(l):

#         res += int(val[i]) ** l

#     if res == j :
#         print(j , end = " ")





# N Armstrong Number 

n = int(input('Enter the no of Armstrong number needed : '))

count = 0

val = 1

while True:

    res = 0

    str_val = str(val)
    l = len(str_val)

    for i in range(l):

        res += int(str_val[i]) ** l

    if res == val :
        print(val , end = " ")
        count += 1

        if count == n:
            break
        
    val += 1