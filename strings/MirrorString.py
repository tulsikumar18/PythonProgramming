# WAP to check the given string can be a mirror string or not.



# Words like AHA and MOM  are strings but MADAM is not mirror string..


## First we will find out all the strings that can be mirror 

## A H I M O T U V W X Y
## o v w x 
## 0 8 

mirror_chars = 'AHIMOTUVWXYovwx08'

s1 = 'AHA'
s2 = 'MADAM'
s3 = 'MOM'
s4 = 'PIP'  # Not Mirror String


for i in s4:

    if i not in mirror_chars:
        print('Not Mirror String')
        break

else:

    if s1 == s1[::-1]:
        print("Mirror String")

    else:
        print('Not Mirror String')







