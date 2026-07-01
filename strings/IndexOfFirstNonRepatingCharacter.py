    

# WAP to display the first non repeating character along with its index...



# s1 = 'programming'
s1 = ''
s1 = 'swwwiss'


d1 = {}


for i in range(len(s1)):

    for j in range(i+1, len(s1)):

        if s1[i] == s1[j]:
            break

    else:

        print('the first non repeating character is : ', s1[i] , 'and at index ' , i)
        break



'''         

## Approach 2 : using the count method to count the no of occurances.. 

def first_non_repeating_chr(s1):


    for i in range(len(s1)):

        cnt = 0

        for j in range(len(s1)):

            if s1[i] == s1[j]:

                cnt += 1
            
        if cnt == 1:

            return s1[i],i
        

print(first_non_repeating_chr("swwwisss"))



'''  