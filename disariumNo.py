# diarium number : if N = 153 then (1**1 + 5**2 + 3**3) == N then It is a Disarium Number..
#sum of its digits powered by their respective positions is equal to the number itself.


# n = int(input('Enter the n:'))

# str_val = str(n)

# l = len(str_val)
# res = 0

# for i in range(l):

#     res += int(str_val[i]) ** (i+1)
    

# if res == n:
#     print(res , end =" ")





# Disarium No b/w 1 to N


# j = int(input('Enter the range n:'))


# for n in range(1 , j+1):
    
#     str_val = str(n)

#     l = len(str_val)
#     res = 0

#     for i in range(l):

#         res += int(str_val[i]) ** (i+1)
        

#     if res == n:
#         print(res , end =" ")




# N Disarium Number


j = int(input('Enter the count n:'))

count = 0
n = 1
while True:
    
    str_val = str(n)

    l = len(str_val)
    res = 0

    for i in range(l):

        res += int(str_val[i]) ** (i+1)
        

    if res == n:
        print(res , end =" ")
        count += 1

        if count == j:
            break

    n += 1
