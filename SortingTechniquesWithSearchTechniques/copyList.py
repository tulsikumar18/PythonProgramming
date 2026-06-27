l1 = [1, 2, 3,4, 5]

## shallow copy..
l2 = l1.copy()  ## the changes made to one will not affect other..

l2.append('don')
print(l2, l1)       #[1, 2, 3, 4, 5, 'don'] [1, 2, 3, 4, 5]

## Can we perform shallow copy without using the shallow copy..
##  Using the slicing [::]

result = l1[::]

print(result)   #[1, 2, 3, 4, 5]


## copy without using a copy..

l1 = [1, 2, 3,4, 5]

res = []

for i in l1:

    res += [i]

print(res)


## Using the assignment operator.. '='

# Reference Copy.. so changes made in one , reflects in both..as we are making the change in the same memory Address..

res1 = l1 # Here we are providing another name to the list l1 that is res1

print(res1)

res1[0] = 'don'

print(l1,res1)  #['don', 2, 3, 4, 5] ['don', 2, 3, 4, 5] 



## Deep Copy..

## general copy or shallow copy..has no problem in the 1 dimensional , but in the 2 dimension the memory adress remains same..
## so the changes made to one reflects to both...


# l1 = [[1,2],[3,4]]
# l2 = l1.copy()

# print(l1,l2)

# l1[0][0]= 1000

# print(l1, l2)

# [[1, 2], [3, 4]] [[1, 2], [3, 4]]
# [[1000, 2], [3, 4]] [[1000, 2], [3, 4]]


# peform deep copy..
l1 = [[1,2],[3,4]]
import copy

l2 = copy.deepcopy(l1)

print(l1,l2)

l1[0][0]= 1000

print(l1, l2)

# [[1, 2], [3, 4]] [[1, 2], [3, 4]]
# [[1000, 2], [3, 4]] [[1, 2], [3, 4]]