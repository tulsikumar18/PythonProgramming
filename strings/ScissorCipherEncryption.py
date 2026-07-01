
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

    elif ord(i) >= 65 and ord(i) <= 90:

        if ord(i) + shift > 90:
            val = (ord(i) + shift ) % 90
            res += chr(65+val)

        else:
            res += chr(ord(i) + shift)


    elif ord(i) >= 97 and ord(i) <= 122:
    
        if ord(i) + shift > 122:

            val = (ord(i) + shift ) % 122
            
            res += chr(97 + val)

        else:

            res += chr(ord(i) + shift)


print(res)






