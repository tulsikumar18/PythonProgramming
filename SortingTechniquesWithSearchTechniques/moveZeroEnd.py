l1 = [1,0,3,4,6,0,10,0]

## list comprehension to access elem which are not zero , then add/ concatenate the zero with 
# the number of zeroes they are 

res = [x for x in l1 if x!= 0] + [0] * l1.count(0)

print(res)    #[1, 3, 4, 6, 10, 0, 0, 0]



## Approach 2 : 

## AS I find zero, I'll remove it and then append at last..

l1 = [0,1,0,3,4,6,0,0,0,0,0,0,10,0]

for i in l1:

    if i == 0:
        l1.remove(i)
        l1.append(i)

print(l1)    #[1, 3, 4, 6, 10, 0, 0, 0]






