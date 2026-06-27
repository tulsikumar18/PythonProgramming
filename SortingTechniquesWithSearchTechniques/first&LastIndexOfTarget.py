## find the first and last index of the target elements..
## Apporach 1 : using 2 for loops..

l1 = [1,2,3,7,11,3,5,6,3,12,14]

## Approach2 : Using the single for loops... and Inbuilt function..

# target = int(input('Enter the target: '))


# if l1.count(target) == 0:
#     print ('-1,-1')


# first_index = l1.index(target)
# last_index = -1

# for i in range(len(l1)):

#     if target == l1[i]:
#         last_index  = i

# print('First_index: ', first_index)
# print('Last Index ', last_index)


#Approach 3:(IMP) using the function.. and without using inbuilt function..


def first_last_index(l1,target):

    firstIndex = -1 
    lastIndex = -1

    for i in range(len(l1)):

        if l1[i] == target:
            
            if firstIndex == -1:
                firstIndex = i
        
            lastIndex = i

    return firstIndex , lastIndex


l1 = [1,2,3,7,11,3,5,6,3,12,14]
target = int(input('Enter the target: '))

print(first_last_index(l1,target)) ## It will print the output in tuple form.




