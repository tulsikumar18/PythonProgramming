
l1 = [1,2 ,3, 4, 5, 6]

## using list comprehension

# val = [x for x in l1 if x % 2 != 0]
# print(val)


# res = []
# def oddNo(l):

#     for i in l:
#         if i % 2 != 0:
#             res.append(i)

# oddNo(l1)
# print(res)



## using lambda function 

# val1 = lambda n : [x for x in n if x % 2 != 0]

# print(val1(l1))



## second output

# val = [x*2 for x in l1]
# print(val)


## third output

# val = [x for x in l1 ]
# print(val)


## using lambda function..

val = lambda n :sum([x for x in l1 ])

print(val(l1))



print(list(filter(lambda n: n %2 == 1, [1, 2, 3,4,5,6])))   # [1, 3, 5]

## set is unordered, but when the values are between 1 to 10 , it has special property to give 
# values in the ordered form only

print(set(filter(lambda n: n %2 == 1, [1, 2, 3,4,5,6]))) # {1, 3, 5}

# print(dict(filter(lambda n: n %2 == 1, [1, 2, 3,4,5,6])))   #TypeError: cannot convert dictionary update sequence element #0 to a sequence


print(str(filter(lambda n: n %2 == 1, [1, 2, 3,4,5,6])))    # <filter object at 0x1049a07f0>







