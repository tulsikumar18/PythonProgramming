
l1 = [1,1,1,2,3,1,1,1,1,4,4,5,1, 1, 1,1,4,5 ]

target = int(input('Target:'))

'''
for i in l1:

    if i == target:
        l1.remove(i)

print(l1)     # [2, 3, 1, 1, 4, 5]

# This is a Wrong Method...as not all target values are removed.. coz the list size is changing
# and the iteration continues index wise...

'''

# Approach 2 : use the count method to count the number of occurance of target element and then
# remove the values till the count of target elem is greater than zero..


'''

while l1.count(target) > 0:
    l1.remove(target)

print(l1)

'''


# Approach 3 : Go Index wise, and then remove the target and then don't increase the index 
# update the index when you are not removing the elements..

 # One pointer Method..
'''
i = 0
while i < len(l1):

    if l1[i] == target:
        l1.remove(l1[i])

    else:
        i+=1

    
print(l1)

'''

## Approach 4 Another method / Method....

'''
while target in l1:

    l1.remove(target)

print(l1)


'''


# Approach 5 : if target matches , shift towards the left ..


l1 = [2,1,1,2,3,1,1,1,1,4,4,5,1,1,1,1,4,5]


i = 0
count = 0
while  i < len(l1):

    if target == l1[i]:

        # shifting Elements towards left 
        count += 1
        for j in range (i , len(l1) - 1):
            l1[j] = l1[j+1]

    else:
        i+=1

print(l1[:len(l1)- count])