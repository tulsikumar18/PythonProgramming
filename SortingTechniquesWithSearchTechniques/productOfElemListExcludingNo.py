# wap to find the product of elements in a list excluding the number in each iteration..



# def productOfElem(l1,prod):
#     res = []
    
#     for i in range(len(l1)):
#         res[i] = prod // l1[i]

#     return res
        



# l1 = [2,4,6,8,10]
# prod = 1

# for i in l1: 
#     prod *= i

# print(productOfElem(l1,prod))



## Apporach 2 : using list comprehension..

l1 = [2,4,6,8,10]
prod = 1

for i in l1: 
    prod *= i

print([ prod // x for x in l1])








