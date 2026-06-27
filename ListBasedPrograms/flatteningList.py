
# Approach 1: if list extend it otherwise append it to the res..
# using inbuilt function ..

# l1 = [1,2,[3,4,5],6,[7,8]]

# res = []

# for i in l1:

#     if type(i) == list:

#         res.extend(i)
#     else:
#         res.append(i)

# print(res)



# Approach 2 : 
# without using the inbuilt function 

l1 = [1,2,[3,4,5],6,[7,8]]

res = []

for i in l1:

    if type(i) == list:

    # fetch one by one value from the nestted list and the append it to the res

        for j in i : 
            res.append(j)
    else:
        res.append(i)

print(res)