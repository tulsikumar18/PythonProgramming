
# WAP to divide the string based on the integer values , when we followed the given conditions


# remove  all the spaces..
# count the total length
# Based on the count , find its squre root 

# then divide the length based on the square root values , that we have got..


s1 = "Ever@#!#ything is Fair #$# in @#$#%^ love and war 3$#$"

## remove the space..

# for i in s1:
#     if i  == " ":
#         continue
#     else:
#         s2 += i


s2 = s1.replace(" ", "")
print(s2)

## find the length of s2
l = len(s2)

## find the sqr_root of l and round it off to nearest integer

sqr_root_val = l ** 0.5
new_val = round(sqr_root_val)
print(new_val)


##print every n no of characters for new_val no of times..using the slicing ..

# for i in range(new_val):

#     print(s2[i*new_val:(i+1)*new_val])




## step value as new_val 

# res1 = ""

# for i in range(0,len(s2),new_val):

    

   

#     print()









'''

## Approach 2 : add the \n at the end of every count of sqr root val.. and at last print s2..


res = ""
count = 0
for i in range(len(s2)):

    if(new_val == count):
        res += '\n'
        count = 0

    count += 1
    res += s2[i]

print(res)


'''