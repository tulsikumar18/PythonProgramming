# Way to take input in the list


# n = int(input('n:'))

# l1 = []

# for i in range(n):

#     val = int(input('Val: '))
#     l1.append(val)
# print(l1)


# 2nd Approach Using List comprehension 
# n = int(input('n:'))

# l1 = [int(input("val :")) for x in range(n)]
# print(l1)



# Now for taking Heterogeneous input in the list

# n = int(input("n: "))
# l1 = eval(input())[:n]   # slicing done to control the number of elements in the list 

# print(l1, type(l1))      #(2, 3, 5, 6)  <class 'tuple'>


# This is how it takes output
# n: 4
# (2, 3, 5, 6)
# (2, 3, 5, 6) <class 'tuple'>



# prod of list Elem 

# l1 = [ 2, 3, 5, 9]

# prod = 1

# for i in l1:

#     prod *= i
# print(prod)


# subtract the elements of list
l1 = [ 2, 3, 5, 9 ]

# the problem arises when the list is empty 
if len(l1) > 0:
    sub = l1[0]

    for i in range(1,len(l1)):   # Here we can also use  for i in l1[1: ] , iterable methodin

        sub -= l1[i]

    print(sub)

