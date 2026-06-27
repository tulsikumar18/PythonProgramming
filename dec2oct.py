n = int(input('Enter the the octal number '))
res = 0
p = 1
while n!= 0:

    rem  = n%8

    res += rem * p
    n //= 8 

    p *= 10

print(res , end =" ")