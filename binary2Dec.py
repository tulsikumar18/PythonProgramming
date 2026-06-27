# Binary to Decimal conversion .. (for n = 7)
#p   4 2 1
#rem 1 1 1

n = int(input('Enter the binary value: '))
decimal = 0

p = 1

while n > 0:

    rem = n % 10
    decimal += rem * p
    n //= 10
    p *= 2

print(decimal)


