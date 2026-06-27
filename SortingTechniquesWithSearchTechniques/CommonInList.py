## Approach 1 : find the intersection of set and then convert it into list..

l1 = [1,2,3,4,5,6,100,200,200]
l2 = [100,200,300 ,200,400,1,4,2000]

# convert it into set and then find intersection ..

# print(list(set(l1).intersection(set(l2))))


### Approach 2 : iterate over loop l1 and then check if the elem is present in l2 or not..also the elem should not
## be present in the res..

res = []

for i in l1:
    
    if i in l2 and i not in res:

        res.append(i)

print(res)
