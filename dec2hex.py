
n = int(input('Enter the decimal val: '))

hex_chars = '0123456789ABCDEF'

hexadecimal = ""

while n != 0:

    rem = n % 16

    hexadecimal += hex_chars[rem]

    n//=16

print(hexadecimal)