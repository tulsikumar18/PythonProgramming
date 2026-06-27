# n = int(input('Enter the number: '))

res = 0

# Approch 1
# this has a time complexity of O(N)

# for i in range(1,n+1):

#     res += i

# print('The total sum is:', res)


# Approach 2  T.E = O(1)

# res = (n*(n+1)/2)

# print('The total sum is:', res)




# Using the List comprehension..

n = int(input('Enter the number: '))

print(sum([x for x in range(1,n+1)]))