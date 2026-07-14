## Remove the duplicates from a sorted list ..

## Approach 1 : using set() - array doesn't need to be sorted...
## Approch 2: using the another list and appending the values if it not present in the new list.

## Approach 3 : Using 2 pointers approach ..

def removeDuplicates(l1):

    if len(l1) < 2:
        return l1


    i = 0
    j = 1

    while j < len(l1):

        if l1[i] != l1[j]:
            
            i+=1
            l1[i] = l1[j]

        j+=1
    return l1[:i+1]



l1 = [1,1, 2,3, 3, 4, 5,5]

print(removeDuplicates(l1))