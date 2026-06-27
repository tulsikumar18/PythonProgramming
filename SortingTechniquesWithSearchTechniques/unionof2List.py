### WAP a program to find the union of the two list..

## Approach 1 : convert it into set and then find union and then convert it back to list..
l1 = [1,2,3,4,5,6]
l2 = [5,6,7,8,1]


# print(list(set(l1).union(set(l2))))



## Approach 2 : 

def union_list(l1,l2):

    for i in l2:

        if i not in l1:
            l1 += [i]

    return l1



l1 = [1,2,3,4,5,6]
l2 = [5,6,7,8,1]

print(union_list(l1,l2))


### Approach 3 : using the set()

l1 = l1+l2
l1 = list(set(l1))

print(l1)