
# WAP to check, the given string can become a strong password or not


# min 8 chars, and less then 30
# 1 upper
# 1 Lower
# 1 numeric
# 1 special char



def strong_pswd(s1):

    if len(s1) < 8 and len(s1) >= 30:
        return False
    
    upper, lower, numeric , sp_chr = 0,0,0,0 ## for unpacking  , the no of integers = no of variable


    for i in s1:

        if ord(i)>= 65 and ord(i) <= 90:
            upper += 1
        elif ord(i) >= 97 and ord(i) <= 122:
            lower += 1
        elif ord(i) >= 48 and ord(i) <= 57 :
            numeric += 1
        else:
            sp_chr += 1

    if upper >= 1 and lower >=1 and numeric >= 1 and sp_chr >= 1:
        return True
    else:
        return False
    

s1 = input('Enter the password : ')

if strong_pswd(s1):

    print('Strong Password')
else:
    print('Not strong Password.')



