## wap to check the given strings is panagram strings or not..

# Panagram Strings: all characters from A to Z should be present in the string..


s1 = "The Quick brown fox jumps over the lazy dog"

s2 = "Pack my box with five dozen liquor jugs"

## Approach 1 : store the freq of each element in the dictionary..in the lower case 
## At last i took a lower case range to check whether the char for a to z is present as keys or not


def panagram(s1):

    freq = {}

    for i in s1:

        char = i.lower()

        if char not in freq:

            freq[char] = 1

        else:

            freq[char]+=1


    for i in range(97 , 123):

        if chr(i) not in freq.keys():
            return False

    return True


if(panagram(s2)):
    print('Panagram')
    
else:
    print("Not Panagram")






'''
## Approach 2 : use set to add the elements and the after converting it into lower.. then check its length is 
## 26 or not..


set2 = set()

for i in s1: 

    if i == " " : 
        continue

    else:
        set2.add(i.lower())


if len(set2) == 26 :
    print('Panagram')
else:
    print('Not panagram')


    '''