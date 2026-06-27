# Decimal to binary conversion .. (for n = 7)
#p   4 2 1
#rem 1 1 1

n = int(input('Enter the binary value: '))

binary = 0

p = 1

while n > 0:

    rem = n % 2
    binary += rem * p
    n //= 2
    p *= 10

print(binary)