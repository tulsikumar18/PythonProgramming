
## Approach 1 : use slicing of len l2 to check 

def secListIsChildOfFirst(l1,l2):

    for i in range(len(l1)):

        if l1[i: i+len(l2)] == l2:
            return True
        
    return False




l1  = [1,2,3,4,5,6,7,8]

l2 = [3,4,5]

if secListIsChildOfFirst(l1,l2):

    print("l2 is a child of l1")

else:
    print('L2 is not child of l1')







