
l1 = ['8','l','@','1','u','h','$','a','9','!','r','2','r']  # this is homogenous list..(only string.)

''' g
create a list which accepts the total values from the count
assigns all the chars & numbers to new list..
reverse the new list
assign the elm from new list to old list 
'''
# ASCII
# 0 - 48, 9=57 , a - 97 , A = 65 , Z = 90 , a= 97, z = 122, 


 ## Approch 1: 

new_list  = []
## append every char to new_list..

for i in l1:

    if (ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):

        new_list.append(i)


## reverse of new_list
# n = len(new_list)
# for i in range(n):

#     new_list[i],new_list[n-i-1] = new_list[n-i-1],new_list[i]

new_list = new_list[::-1]
print(new_list)

## assigns it to new list..

i = 0
j = 0

while i < len(l1):

    if (ord(l1[i]) >= 48 and ord(l1[i]) <= 57) or (ord(l1[i]) >= 65 and ord(l1[i]) <= 90) or (ord(l1[i]) >= 97 and ord(l1[i]) <= 122):

        l1[i] = new_list[j]
        j+=1
        i+=1

    else:
        i+=1
    
print(l1)



        
## Approach 2 :  // Assignment..

def is_num_or_char(n):

    pass


for i in range(len(l1)):

    if is_num_or_char(l1[i]) == is_num_or_char(l1[j]):

        pass

        # swap the ith value and jth value..

    # decrement j and increment i;





