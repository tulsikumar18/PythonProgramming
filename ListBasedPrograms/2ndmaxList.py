'''

l1 = [10,5,3,8,4,80,7,80]

# With using inbuilt methods.. 

# it has 2 80 so , it will give l1[-2] as 80 only so use set() to remove the duplicates

res = list(set(l1))

res.sort()

print(res[-2])

'''


''' 
Approach 2 : when the larget element is repeated then we access the 2nd largest elem l1[-2] then 
wrong output we will get..

if len(l1) == 0:
    print("empty List")
elif len(l1) == 1:
    print(l1[0])
else:
    j = len(l1)-1
    max = l1[-1]
    res = l1[-1]

    while res == max:
        res = l1[j]
        j -= 1
        
    print(l1[j]) # this index will have the 2nd largest element..

'''

# Without using the inbuit methods..

l1 = [10,5,3,8,4,80,7,80]

l1 = [10,2,5,2]

if len(l1)>0:

    max1 = -1
    max2 = -1

    for val in l1:

        if val > max1:
            max2 = max1
            max1 = val
        elif max1 > val > max2:
            max2 = val

    print(max2)


