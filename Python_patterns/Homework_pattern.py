# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4


# n = int(input('n:'))
# val = 1
# for i in range(n):

#     for j in range(n):

#         if(i >= j):
#            print(val , end = " ")

#     print()
#     val += 1




# # 1 
# # 1 2 
# # 1 2 3 
# # 1 2 3 4


# n = int(input('n:'))

# for i in range(n):
#     val = 1

#     for j in range(n):

#         if(i >= j):
#            print(val , end = " ")
#            val += 1

#     print()
   






# # 1 
# # 2 3 
# # 4 5 6 
# # 7 8 9 1


# n = int(input('n:'))
# val = 1
# for i in range(n):

#     for j in range(n):

#         if(i >= j):
#            print(val , end = " ")
#            val += 1

#            if val > 9:
#                val = 1

#     print()
   





# A 
# B B
# C C C 


# n = int(input('n:'))
# val = 65
# for i in range(n):

#     for j in range(n):

#         if(i >= j):
#            print(chr(val) , end = " ")

#     val += 1
#     print()
   



# A 
# A B
# A B C 


# n = int(input('n:'))

# for i in range(n):
#     val = 65
#     for j in range(n):

#         if(i >= j):
#            print(chr(val) , end = " ")
#            val += 1

    
#     print()







# A 
# B C
# C D E 


# n = int(input('n:'))
# val = 65
# for i in range(n):

#     for j in range(n):

#         if(i >= j):
#            print(chr(val) , end = " ")
#            val += 1

    
#     print()




# # 4
# # 3 3 
# # 2 2 2 
# # 1 1 1 1


# n = int(input('n:'))
# val = n
# for i in range(n):
   
#     for j in range(n):

#         if(i >= j):
#            print(val, end = " ")
    
#     val -=1

#     print()





# 4
# 4 3 
# 4 3 2
# 4 3 2 1


# n = int(input('n:'))

# for i in range(n):
#     val = n
#     for j in range(n):

#         if(i >= j):
#            print(val, end = " ")
#            val -=1

#     print()





# Z
# Z X
# Z X Y
# Z X Y W


# n = int(input('n:'))

# for i in range(n):
#     val = ord('Z')
#     for j in range(n):

#         if(i >= j):
#            print(chr(val), end = " ")
#            val -=1

#     print()





# D
# C B
# A D C
# B A D C


# n = int(input('n:'))
# val = ord('A') + n - 1
# for i in range(n):
    
#     for j in range(n):

#         if(i >= j):
#            print(chr(val), end = " ")
#            val -=1
#            if val < ord('A'):
#                 val = ord('A') + n - 1

    
    
    
#     print()




# A A A A 
#   B B B 
#     C C 
#       D


# n = int(input('n:'))
# val = ord('A') 
# for i in range(n):
    
#     for j in range(n):

#         if j >= i :
#             print(chr(val), end= " ")

#         else:
#             print(" ", end= " ")

    
#     val += 1
    
#     print()




# A B C D 
#   E F G 
#     H I
#       J


# n = int(input('n:'))
# val = ord('A') 
# for i in range(n):
    
#     for j in range(n):

#         if j >= i :
#             print(chr(val), end= " ")
#             val += 1

#         else:
#             print(" ", end= " ")

    
#     print()





# 4 3 2 1
#   4 3 2 
#     4 3 
#       4


# n = int(input('n:'))

# for i in range(n):
#     val = n
#     for j in range(n):

#         if j >= i :
#             print(val, end= " ")
#             val -= 1

#         else:
#             print(" ", end= " ")

    
#     print()







# # Z Y X W
# #   Y X W
# #     X W
# #       W


# n = int(input('n:'))
# val = ord('Z') + 1
# val2 = val
# for i in range(n):
#     val = val2 - 1
#     for j in range(n):
       
#         if j >= i :
            
#             print(chr(val), end= " ")
#             val -= 1

#         else:
#             print(" ", end= " ")

#     val2 -=1


    
#     print()




# # 1 
# #     *
# #         2
# #             *


# n = int(input('n:'))
# val = 1

# for i in range(n):
   
#     for j in range(n):

#         if i == j:
            
#             if i % 2 == 0 & j % 2 == 0:
#                 print(val, end = " ")
#                 val += 1

#             else:
#                 print("*", end=" ")
               
#         else:
#             print(" ",end =" ")
    
#     print()







# #             1
# #         *
# #     2
# # *


# n = int(input('n:'))
# val = 1

# for i in range(n):
   
#     for j in range(n):

#         if i + j == n-1:
            
#             if i % 2 == 0 & j % 2 == 0:
#                 print(val, end = " ")
#                 val += 1

#             else:
#                 print("*", end=" ")
               
#         else:
#             print(" ",end =" ")
    
#     print()






#          A
#      B   B
#   C  C   C


# n = int(input('n:'))
# val = ord('A')

# for i in range(n):
   
#     for j in range(n):

#         if i + j >= n-1:
#             print(chr(val), end=" ")

#         else:
#             print(" ",end = " ")
    
#     val += 1

               
    
#     print()








# #          D
# #       C  C
# #    B  B  B
# # A  A  A  A


# n = int(input('n:'))
# val = ord('A') + n - 1

# for i in range(n):
   
#     for j in range(n):

#         if i + j >= n-1:
#             print(chr(val), end=" ")

#         else:
#             print(" ",end = " ")
    
#     val += 1

               
    
#     print()





# #          D
# #       D  C
# #    D  C  B



# n = int(input('n:'))


# for i in range(n):
#     val = ord('A') + n - 1
#     for j in range(n):

#         if i + j >= n-1:
#             print(chr(val), end=" ")
#             val -= 1

#         else:
#             print(" ",end = " ")
    


               
    
#     print()







#          4
#       4  3
#    4  3  2
# 4  3  2  1



# n = int(input('n:'))


# for i in range(n):
#     val = n
#     for j in range(n):

#         if i + j >= n-1:
#             print(val, end=" ")
#             val -= 1

#         else:
#             print(" ",end = " ")
            
    
#     print()





# # 1 2 3 4
# # 1 2 3 
# # 1 2
# # 1



# n = int(input('n:'))

# for i in range(n):
#     val = 1
#     for j in range(n):

#         if i+ j <= n - 1:

#             print(val, end = " ")
#             val += 1
            
    
#     print()







# # D D D D 
# # C C C C 
# # B B 
# # A



# n = int(input('n:'))
# val = ord('A') + n - 1
# for i in range(n):
    
#     for j in range(n):

#         if i+ j <= n - 1:

#             print(chr(val), end = " ")
#     val -= 1
            
    
#     print()





# # 1 * 2 * 
# # 3 * 4
# # * 5 
# # 6

# # When * and values are mixed.. then take help from variable.

# n = int(input('n:'))
# val = 1
# p = True
# for i in range(n):
    
#     for j in range(n):

#         if i + j <= n - 1:

#             if p:
#                 print(val , end= " ")
#                 val+=1 

#                 # if val > 9 : val = 1

#                 p = False
#             else:
#                 print("*", end = " ")
#                 p = True

#     print()





# A B C D 
# E F G
# H I
# J


# n = int(input('n:'))

# val = ord("A")

# for i in range(n):
    
#     for j in range(n):

#         if i + j <= n - 1:

#             print(chr(val), end = " ")
#             val +=1


#     print()
