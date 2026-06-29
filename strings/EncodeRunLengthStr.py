# WAP to encode a run length of a string..


# Ex : aaaaaabbccccccdddeeefffffgggh

# output : a6b2c6d3e3f5g3h1



s2 = "aaaaaabbccccccdddeeefffffgggh"

'''

## Approach 1 : Take two pointers and then move 2nd one till we get the different one 

res = ""
i = 0
j = 0
while i < len(s2):
    
    count = 0

    while j < len(s2) and (s2[i] == s2[j]) :

        count += 1
        j += 1

    
    res += s2[i]+ str(count)
    i = j

print(res)


'''

# Approach 2 : Using the single loop , also count the character , when it  is not matching , concatenate it , also
## the last character will not be added so add it at the last..


res1 = ""

count = 1

for i in range(len(s2) - 1):

    if s2[i] == s2[i+1]:
        count += 1

    else:

        res1 += s2[i] + str(count)
        count = 1


res1 += s2[-1] + str(count)

print(res1)


    