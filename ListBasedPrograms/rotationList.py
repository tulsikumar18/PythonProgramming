'''
This is one rotation of list 

l1 = [1, 2, 3, 4, 5]

k = 1 # rotoate by one position 


temp = l1[0]

for i in range(len(l1) - 1):
    l1[i] = l1[i+1]

l1[-1] = temp

print(l1)

'''
# Approach 2: 

# For K rotation , run the look for k times..


# now if the k is greater than len(l1) i.e for n = 5 ,like 6 times then the loop will run for 6 times, so it will take more time
# so take modulus to reduce it as we know that after every 5th rotation the list will be same 
# so update the outer loop k = k % len(l1) 

'''
l1 = [1, 2, 3, 4, 5]
k = int(input('Enter the no of rotation: '))

k = k% len(l1)
for val in range(k):

    temp = l1[0]

    for i in range(len(l1) - 1):
        l1[i] = l1[i+1]

    l1[-1] = temp

print(l1)

'''
'''

# Approach 3 : Instead of using two loops we can use list concatenation to get the output
## IMPORTANT APPROACH


l1 = [1, 2, 3, 4, 5]

k = int(input('Enter the no of rotation: '))

k = k % len(l1)

l1 = l1[k: ] + l1[ :k]

print(l1)

'''


'''

AnticlockWise Rotation

l1 = [1,2,3,4,5]

k = 1

o/p = [5,1,2,3,4]




l1 = [1,2,3,4,5]

k = int(input('Enter the no of rotation: '))

k = k % len(l1)

for k in range(k):

    temp = l1[-1]

    for i in range(len(l1) - 1, 0,-1):

        l1[i] = l1[i-1]
    
    l1[0] = temp

print(l1)

'''


# Approach 2 for Anticlock wise..


l1 = [1,2,3,4,5]

k = int(input('Enter the no of rotation: '))

k = k % len(l1) # After every n rotation , it will get same list..

n = len(l1)

# l1 = l1[n-k: ] + l1[ :n-k]
# or 

l1 = l1[-k: ] + l1[ : -k]

print(l1)

