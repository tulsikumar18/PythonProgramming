

n = int(input('Enter the the octal number '))
res = 0
p = 1
while n!= 0:

    rem  = n%10

    res += rem * p
    n //= 10 

    p *= 8

print(res , end =" ")
