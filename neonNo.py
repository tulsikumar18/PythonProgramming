# A Neon Number is a number where the sum of the digits and its square is equal to the
#  original number.


# n = int(input('Enter the number: '))

# sqr_val = n**2
# res = 0

# while sqr_val != 0:

#     rem = sqr_val % 10

#     res += rem 
#     sqr_val //= 10

# if res == n:
#     print(n,end = " ")



# neon no b/w 1 to N

n = int(input('Enter the range of N : '))



for j in range(1,n+1):

    sqr_val = j**2
    res = 0

    while sqr_val != 0:

        rem = sqr_val % 10

        res += rem 
        sqr_val //= 10

    if res == j:
        print(j,end = " ")




# N Neon Number



n = int(input('Enter the no of N : '))

count = 0
val = 1

while True:

    sqr_val = val**2
    res = 0

    while sqr_val != 0:

        rem = sqr_val % 10

        res += rem 
        sqr_val //= 10

    if res == val:
        print(val,end = " ")
        count += 1

        if count == n:
            break

    val +=1