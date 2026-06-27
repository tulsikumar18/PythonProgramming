# Reverse the word in the same place if special character count is even..


s1 = "I@@! am!@$! Pool!!@#$$ Deadpool!@ Here%^#@! to!@ kill!@# Bad!@#$ guys!@@#$@#!"

# output :  I@@! !$@!ma $$#@!!looP @!loopdaeD Here%^#@! @!ot kill!@# $#@!daB !#@$#@@!syug 


# using split method.. I will split it at space..

res = " "


s2 = s1.split()

# print(s1)


for j in s2:

    count = 0

    for i in j :

        if ord(i)>= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122 or ord(i) >= 48 and ord(i) <= 57:
            continue
        else:

            count += 1
    
    # if count is even..

    if count % 2 == 0:

        res += j[::-1] + " "

    else:
        res += j + " "

print(res)
        




