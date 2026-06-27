
'''
## Approach 1 : Reverse the list and then  perform the swapping in the other half..


def ListRotation(l1):
    
    ## Reverse the List..
    l1 = l1[::-1]


    ## find the index of other half.. for which we will do swapping.
    n = len(l1) // 2

    j = len(l1) - 1
    i = n

    while i<=j:
        # swap the elements of other half.. and decrease the index 
        l1[i] , l1[j] = l1[j] , l1[i]
        i+=1
        j-=1

    return l1



l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print(ListRotation(l1))             #[13, 12, 11, 10, 9, 8, 1, 2, 3, 4, 5, 6, 7]

'''




## Approach 2 :  using the slicing method 


def ListRotation(l1):
    

    n = len(l1) // 2

    l1 = l1[n::][::-1] + l1[:n]
    return l1



l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print(ListRotation(l1))      