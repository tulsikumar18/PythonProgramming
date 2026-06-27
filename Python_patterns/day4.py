

#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 


# n = int(input('n:'))

# spc = 0
# str = 2 * n - 1

# for i in range(n):

#     for j in range(spc):

#         print(" " , end = " ")
    
#     for k in range(str):

#         print("*", end = " ")
#     print()

#     spc+=1
#     str-=2





# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 


# Without using the variable
# also another formula that can be used is 2(n-i) - 1

# n = int(input('n:'))


# for i in range(n):

#     for j in range(i):

#         print(" " , end = " ")
    
#     for k in range(2*(n-i)-1):

#         print("*", end = " ")
    
#     print()


# 3  * 
# 2  * * 
# 1  * * * 
# 0  * * * *   get the peak at i = 0 only..
# -1 * * * 
# -2 * * 
# -3 * 


# n = int(input('n:'))


# for i in range(n-1, -n, -1):

    
#     for j in range(n - abs(i)):

#         print("*", end = " ")
    
#     print()




# Space has to be considered here..
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

# n = int(input('n:'))


# for i in range(n-1, -n, -1):


#     for j in range(abs(i)):

#         print(" ", end = " ")

    
#     for j in range(n - abs(i)):

#         print("*", end = " ")
    
#     print()





# * * * * 
# * * * * 
# * * * * 
# * * * * 

# n = int(input('n:'))

# for i in range(n):

#     print("* " * n)


# n:5
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 

# this approach will not work in the column wise changes..

# n = int(input('n:'))
# val = 1
# for i in range(n):

#     print((str(val) + " ")  * n)    # Here string concatenation and string repetation takes place..

#     val +=1



# n:4
# * 
# * * 
# * * * 
# * * * * 

# n = int(input('n:'))

# for i in range(1,n+1):

#     print("* " * i)


#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# n = int(input('n:'))

# for i in range(1,n+1):

#     print( "  " * (n-i) + "* " * i)    # use the two space... for proper alignment




# * * * * 
# * * * 
# * * 
# * 

# n = int(input('n:'))

# for i in range(n):

#     print("* " * (n-i)) 



#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
# * * * * * * * * * * * 


# n = int(input('n:'))

# for i in range(n):

#     print("  " * (n-i-1) + "* " * (2 * i + 1))    # use two space for proper alignment



# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 


# n = int(input('n:'))

# for i in range(n):

#     print("  " * i +  "* " * (2*(n-i)-1))



# pascals Triangle..