# l1 = [1,3, 5, 9,10]

# res = 0

# for i in l1:

#     res += i

# print('The Sum is ', res)


# For Heterogeneous Data type..

# l1 = [1,3, 5, 9,10, 'don', 1+2j, 1.3]

# res = 0

# for i in l1:
    
#     if type(i) == int or type(i) == float :

#         res += i

# print('The Sum is ', res)




# For Heterogeneous list , we can also use the isinstance() method to check whether it is value is instance/obj
# of the class varible..

a = 4 
b = 4.7
c = True

print(isinstance(a, int))
print(isinstance(b, int))



# instead of one by one we can use tuple to check it in one way 

print(isinstance(a,(tuple, int, bool))) # Here the a type is int so it will return true

# also the type of true is int also , coz boolean comes under the int data type in python 

print(isinstance(c, int)) # True    