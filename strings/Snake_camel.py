s1 = 'if_you_are_good_at_something_never_do_it_for_free'

## SnakeCase to CamelCase

## Approach 1 : 
## use third variable to track the underscore.. , if the found == True, which means the the prev elem was 
## underscore, it that case concatenate the upper case char..



## Appraoch 2 : use the index to check the  previous elem , if the prev elem is underscore then we will
## concatenate the uppercase character...


res = ''

found = False

for i in range(len(s1)):

    ## if it is the first elem , convert it into uppercase and then concatenate..

    if i == 0:
        res += chr(ord(s1[i]) - 32)

    elif  ord(s1[i]) >= 97 and ord(s1[i]) <= 122 and found:
        res += chr(ord(s1[i]) - 32)
        found = False

    elif ord(s1[i]) >= 97 and ord(s1[i]) <= 122 and found == False:
        res  += s1[i]

    else:
        res += " "
        found = True

print(res)
