# # Pattern 8
# # A A A A
# # B B B B
# # C C C C 
# # D D D D 

# # Using ord() and chr() Method..

# row = int(input('Row: '))
# col = int(input('Col:'))

# val = ord('A')

# for i in range(row):

#     for j in range(col):

#         print(chr(val) , end = " ")
    
#     print()
#     val += 1
# # if val > ord('Z') then it will some other characters, so make it again 65..
#     if val > ord('Z'):
#         val = ord('A')




# Pattern 9
# A B C D
# A B C D
# A B C D
# A B C D

# Using ord() and chr() Method..

# row = int(input('Row: '))
# col = int(input('Col:'))

# for i in range(row):
#     val = ord('A')

#     for j in range(col):

#         print(chr(val) , end = " ")
#         val += 1
#         # if val > ord('Z') then it will some other characters, so make it again 65..
#         if val > ord('Z'):
#             val = ord('A')
    
#     print()
   

# pattern 10
# A B C D
# E F G H
# I J K L

# row = int(input('Row: '))
# col = int(input('Col:'))

# val = ord('A')
# for i in range(row):

#     for j in range(col):

#         print(chr(val) , end = " ")
#         val += 1
#         # if val > ord('Z') then it will some other characters, so make it again 65..
#         if val > ord('Z'):
#             val = ord('A')
    
#     print()
   




# pattern 11
# 4 4 4 4
# 3 3 3 3
# 2 2 2 2
# 1 1 1 1

# row = int(input('Row: '))
# col = int(input('Col:'))
# val = row

# # if row > 9 , start from 9 only
# if val > 9:
#     val = 9

# for i in range(row):

#     for j in range(col):

#         print(val, end  = ' ')
#     print()
#     val -=1

#     # to prevent from negative values(-1, etc..)
#     if val < 1:
#         val = 9



        
 
   
# pattern 12
# column wise..
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1 

# row = int(input('Row: '))
# col = int(input('Col:'))

# for i in range(row):
#     val = col
#     for j in range(col):

#         print(val, end  = ' ')
#         val -= 1

#     print()
    



# pattern 13
# N X N (n = 5 )
# 01 02 03 04 05
# 06 07 08 09 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# n = int(input('n:'))
# # convert it into str to find its length , so that zfill can be accomodated to fill 0 based on the length(last digit)
# w = len(str(n**2))
# val = 1

# for i in range(n):
#     for j in range(n):

#         print(str(val).zfill(w), end  = ' ')
#         val +=1

#     print()




# #pattern 14
# # N X N (n = 3 )
# # z z z z 
# # y y y y 
# # x x x x


# n = int(input('n:'))

# val = ord('z')

# for i in range(n):
#     for j in range(n):

#         print(chr(val) , end = ' ')
        
#     val -=1

#     # when val < ord('a')  make it again z

#     if(val < ord('a')):
#         val = ord('z')

#     print()




#pattern 15

n = 4
# D D D D 
# C C C C 
# B B B B 
# A A A A


# n = int(input('n:'))

# val = ord('A') + n - 1 # as the last if 65 + 4 = 69 which is equal to E but it should have been D only..so -1

# for i in range(n):
#     for j in range(n):

#         print(chr(val) , end = ' ')
        
#     print()
#     val -=1

    

# pattern 16

# n= 5
# 1 1 1 1 
# * * * * 
# 2 2 2 2 
# * * * * 
# 3 3 3 3 


# n = int(input('n: '))

# val = 1

# for i in range(n):

#     for j in range(n):

#         if i % 2 == 0:
#             print(val, end= " ")
#         else:
#             print('*' , end = ' ')
    
    
#     if(i%2 == 0):
#         val += 1
#     print()



# # pattern 17
# 1 * 2 * 3 
# 1 * 2 * 3
# 1 * 2 * 3
# 1 * 2 * 3
# 1 * 2 * 3


# n = int(input('n: '))

# for i in range(n):

#     val = 1
#     for j in range(n):

#         if j % 2 == 0:
#             print(val, end= " ")
#             val += 1
#         else:
#             print('*' , end = ' ')
    
#     print()





# # pattern 18
# Here it is a mixture of values and *... so take help from the help from the third variable p

# 1 * 2 * 3 
# * 4 * 5 * 
# 6 * 7 * 8 
# * 9 * 1 * 
# 2 * 3 * 4


# n = int(input('n: '))
# val = 1
# p = True
# for i in range(n):

#     for j in range(n):

#         if p:
#             print(val, end= " ")
#             val += 1
#             p = False
#             # if val > 9:val = 1     # this can be done in one line only..for just one statement only.

#             if val>9:
#                 val = 1
                
#         else:
#             print('*' , end = ' ')
#             p = True
    
#     print()



# Assignment three patterns..

# A A A A 
# * * * * 
# B B B B
# * * * *  


# n = int(input('n:'))
# val = ord('A')
# for i in range(n):
    
#     for j in range(n):

#         if i % 2 == 0:

#             print(chr(val), end = " ")

#         else:
#             print("*", end = " ")
    

#     if  i % 2 == 0:
#         val += 1


#     print()




# A * B * 
# A * B * 
# A * B * 
# A * B * 

# n = int(input('n:'))

# for i in range(n):
#     val = ord('A')
#     for j in range(n):

#         if j % 2 == 0:

#             print(chr(val), end = " ")
#             val += 1

#         else:
#             print("*", end = " ")


#     print()







# A * B 
# * C * 
# D * E



# # When * and values are mixed.. then take help from variable.

# n = int(input('n:'))
# val = ord('A')
# p = True
# for i in range(n):
    
#     for j in range(n):

#             if p:
#                 print(chr(val) , end= " ")
#                 val+=1 

#                 # if val > 9 : val = 1

#                 p = False
#             else:
#                 print("*", end = " ")
#                 p = True

#     print()





# for a 5 X 5 matrix i and j values varies as In this for 

# i == j : for Diagonal Elements

# i > j : for left lower right angle triangle

# i < j : for right upper right angle triangle


# 00 01 02 03 04
# 10 11 12 13 14
# 20 21 22 23 24
# 30 31 32 33 34
# 40 41 42 43 44


# pattern 

# *         
# * *       
# * * *     
# * * * *   
# * * * * * 

# n = int(input('n:'))

# for i in range(n):

#     for j in range(n):

#         if i >= j :
#             print('*', end = " ")

#         else:
#             print(' ' , end= " ")

#     print()







# I+J summation..

# 0 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6 
# 3 4 5 6 7
# 4 5 6 7 8



# Pattern  ( i + j == n-1 ) since it starts from 0 

#           * 
#         *   
#       *     
#     *       
#   *         
# *     


# n = int(input('n:'))

# for i in range(n):

#     for j in range(n):

#         if i + j == n-1:
#             print('*', end = " ")

#         else:
#             print(' ' , end= " ")

#     print()



# pattern 

# * * * * * * * 
# * * * * * *   
# * * * * *     
# * * * *       
# * * *         
# * *           
# *     

# n = int(input('n:'))

# for i in range(n):

#     for j in range(n):

#         if i + j <= n-1:
#             print('*', end = " ")

#         else:
#             print(' ' , end= " ")

#     print()




# pattern 

#             * 
#           * * 
#         * * * 
#       * * * * 
#     * * * * * 
#   * * * * * * 
# * * * * * * * 


# n = int(input('n:'))

# for i in range(n):

#     for j in range(n):

#         if i + j >=  n-1:
#             print('*', end = " ")

#         else:
#             print(' ' , end= " ")

#     print()
