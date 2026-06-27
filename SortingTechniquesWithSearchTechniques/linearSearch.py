'''
Approach 1 : 

l1 = [10,2, 5, 8, 3, 4]

key = int(input('Enter the target : '))
found  = False

for i in range(len(l1)):

    if key== l1[i]:

        print(f' The Key {key} is found at index {i}')
        found = True
        break

if found == False:
    print(f'Key { key} is not found in the list')


# this will be used with the while loop only..

if i >= len(l1):

    print(f'Key { key} is not found in the list')





## Approach 2 : using for and else..

# else block gets executed only when the loop gets completely executed..
## and the loop will completely executed only when the key is not present...



l1 = [10,2, 5, 8, 3, 4]

key = int(input('Enter the target : '))

for i in range(len(l1)):

    if key== l1[i]:

        print(f' The Key {key} is found at index {i}')
        break
else:
    print(f'Key { key} is not found in the list')


'''

## When it is asked about the 2nd occurance of the key..




l1 = [10,2, 5, 8, 3, 5,4]

key = int(input('Enter the target : '))

## take the number of occurance to be searched..every time we find the key ,
# increase the count by 1 till we get the nth occurance..

nth = int(input('Enter the occurance..'))

count = 0 
found  = False

for i in range(len(l1)):

    if key== l1[i]:
        count += 1
        if count == nth:
            print(f' The Key {key} is found at index {i}')
            found = True
            break

if found == False:
    print(f'{count+1}th occurance of the key { key} is not found in the list')