
# WAP to convert the string based on the below condition 


# if the length is even , and  the if the ASCII value of character is even then convert to '@' 
# and space character to  '#'

## if the length is odd and  the if the ASCII value of character is 
#  odd then convert  to '$' and space char to '^'..



def length(s2):
    count = 0

    for i in s2:

        if i == " ":
            continue
        else:

            count += 1

    return count


s2 = 'I Love Programming in Python'

# output..:
# I#@o@e#@@og@ammi@g#i@#@y@@o@

res1 = ""

print(length(s2))


if length(s2) % 2 == 0:

    for i in s2:

        if  i == " ":
            res1 += '#'

        elif ord(i) % 2 == 0:
            res1 += '@'

        else:
            res1 += i

else:

    for i in s2:
        if i == " " :
             res1 += '^'
     
        elif ord(i) % 2 != 0:
            res1 += '$'

        else:

            res1 += i

print(res1)




