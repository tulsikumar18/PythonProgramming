# Wap to display the longest word in the given sentence



### Approach 1 : 

#  use split method..

s1 = 'always do good to othersss it will come back in unexpected ways'

# s1 = ""

if len(s1) == 0:
    print('','0')
    exit()

s2 = s1.split()

# print(s2)


maxi  = 0

for i in range(len(s2)):

    if len(s2[i]) > len(s2[maxi]): 

        maxi = i
    
    else:
        continue

print('The longest word is : ', s2[maxi] ,'\nand the length is : ', len(s2[maxi]))




## Approach 2 : 