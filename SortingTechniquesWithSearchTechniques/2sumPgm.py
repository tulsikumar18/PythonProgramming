
## Brute Force Approach 
# O(N**2)

'''
def Two_sum(l1):

    target = int(input('Enter the target: '))

    for i in range(len(l1)):

        val = target - l1[i]
        for j in range(i+1,len(l1)):

            if val == l1[j]:
                return i,j


l1 = [2,1,3,6,5,1,4]
if len(l1) < 2: 
    print(-1,-1)
print(Two_sum(l1))




## Approach 2 : 

def Two_sum(l1):

    target = int(input('Enter the target: '))

    for i in range(len(l1)):

        val = target - l1[i]
        for j in range(i+1,len(l1)):

            if val == l1[j]:
                return i,j


l1 = [2,1,3,6,5,1,4]
print(Two_sum(l1))

'''

### Approach 3 :  IMPORTANT
### using a dictionary to store the value and index , which is seen..

###  TIME COMPLEXITY O(N)
### SPACE COMPLEXITY = O(N)

 

def Two_sum(l1):

    target = int(input('Enter the target: '))

    seen = {}
    for i in range(len(l1)):

        val = target - l1[i]

        if val in seen:
            return seen[val],i
        
        seen[l1[i]] = i

    return -1,-1
       


l1 = [2,1,3,6,5,1,4]

print(Two_sum(l1))

