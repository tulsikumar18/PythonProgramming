

### check whether it is palindrome or not..

## approach , use slicing and then reverse function


## approch 2 : use two pointer apporach..
'''

def is_palindrome(s1):

    i = 0
    j = len(s1) - 1

    while(i <= j):

        if s1[i] != s2[j]:
            return False
            break
        
        i += 1
        j -= 1
    return True



s2 = input('Enter the string : ')

if(is_palindrome(s2)):

    print('Palindrome')

else:
    print('Not Palindrome')

'''

## Approach 3 : If you are using a for loop , use the else with it..


def is_palindrome(s1):

    i = 0
    j = len(s1) - 1

    for i in range(len(s1)):

        if s1[i] != s2[j]:
            return False
            break
        
        j -= 1
   
    else:
        return True
    


s2 = input('Enter the string : ')

if(is_palindrome(s2)):

    print('Palindrome')

else:
    print('Not Palindrome')




