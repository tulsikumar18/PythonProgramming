
# wap to encode a given string as follows....

s1 = 'Hide the Deadbodyz'

# shift = 4 

# y when encoded to 121 + shift = 125 % 122  = 3 ( c)

# Scissor shifer Encryption 

res = ""
shift = int(input("Enter the shift .."))

for i in s1:

    if i == " ":
        res += " "

    elif ord(i) + shift > 122:

        val = (ord(i) + shift ) % 122
        
        res += chr(97 + val)

    else:

        res += chr(ord(i) + shift)


print(res)


