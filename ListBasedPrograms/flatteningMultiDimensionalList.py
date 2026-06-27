
# stack is used to manage function call 


# 0 1, 2, 3, 4 , 3, 2, 1, 0

# without using loop
# using recursion

'''
def func(n):

    if n < 4: 

        print(n, end = " ")
        func(n+1)
    print(n, end = " ")

print('start')

func(0)
print('\nEnd')



output 
start
0 1 2 3 4 3 2 1 0 
End

'''


# Factorial function using recursion 



# def func(n):

#     if n <= 1: 
#         return 1
    
#     return n * func(n-1)


# print(func(5))



''''
# Assignments using recursion 

binary to decimal 
sum of 1 to N 

'''


# flattening the multidimensional list using recursion..( Can be done using Recursion )

## Approach 1 : outplace Algorithm..

l1 = [[1],2,[3,[4,5,6],5],6,[7,[8]]]

res = []

def flatteningList(l1):

    for i in l1:

        if type(i) != list:
            res.append(i)

        else:
        
            flatteningList(i)

flatteningList(l1)

print(res)

