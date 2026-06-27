
### Approach 1 : swapcase() : inbuilt method to convert the case of the string..


## Approach 2 :  using the ord() and chr() function

s1 = 'Python Coding is Awesome'

res = ''

for i in s1:

    if ord(i)>= 65 and ord(i) <= 90:
        res += chr(ord(i) + 32)
    elif ord(i) >= 97 and ord(i) <= 122:
        res  += chr(ord(i) - 32)
    else:
        res += " "

print(res)


