    #             *
    #         *    *   *
    #     *   *   *    *   * 
    # *   *    *  *     *   *    * 


# space decreases and the star increases
# Use one loop for space and then one for the stars..

# n = int(input('n:'))

# spc = n - 1
# str = 1

# for i in range(n):

#     for j in range(spc):

#         print(" " ,end = " ")

#     for k in range(str):

#         print("*" , end = " ")

#     print()
#     spc -= 1

#     str += 2

       




# # Without using the third variable..
# stars = 2*i + 1
# space = n - 1 - i

# n = int(input('n:'))

# for i in range(n):

#     for j in range(n-1-i):
#         print(' ', end = " ")

#     for k in range(2 * i + 1):

#         print("*", end = " ")
    
#     print()

        


# assignment 3

    #       1 
    #     2 2 2 
    #   3 3 3 3 3 
    # 4 4 4 4 4 4 4 

# n = int(input('n:'))
# val = 1
# for i in range(n):

#     for j in range(n-i-1):

#         print(" ", end = " ")

#     for k in range(2*i + 1):

#         print(val, end=" ")

#     print()

#     val +=1



# pattern

#       1 
#     1 2 3 
#   1 2 3 4 5 
# 1 2 3 4 5 6 7 


# n = int(input('n:'))

# for i in range(n):
#     val = 1
#     for j in range(n-i-1):

#         print(" ", end = " ")

#     for k in range(2*i + 1):

#         print(val, end=" ")
#         val +=1

#     print()

    



#         5 
#       5 4 3 
#     5 4 3 2 1 
#   5 4 3 2 1 0 5 
# 5 4 3 2 1 0 5 4 3 


# n = int(input('n:'))

# for i in range(n):
#     val = n
#     for j in range(n-i-1):

#         print(" ", end = " ")

#     for k in range(2*i + 1):

#         print(val, end=" ")
#         val -=1

#         if val < 0:
#             val = n

#     print()




#       A 
#     B B B 
#   C C C C C 
# D D D D D D D 

# n = int(input('n:'))
# val = ord('A')
# for i in range(n):
    
#     for j in range(n-i-1):

#         print(" ", end = " ")

#     for k in range(2*i + 1):

#         print(chr(val), end=" ")
        

#     val +=1

#     print()



#       D 
#     C C C 
#   B B B B B 
# A A A A A A A 

# n = int(input('n:'))
# val = ord('A') + n - 1
# for i in range(n):
    
#     for j in range(n-i-1):

#         print(" ", end = " ")

#     for k in range(2*i + 1):

#         print(chr(val), end=" ")
        

#     val -=1

#     print()

# 1 1 1 1 1 1 1 
#   2 2 2 2 2 
#     3 3 3 
#       1 

# n = int(input('n:'))
# val = 1
# for i in range(n ,0 ,-1):


#     for j in range(n-i):

#         print(" ", end = " ")

#     for k in range(2*i - 1):

#         print(val, end=" ")
    

#     val +=1
#     if val > n - 1:
#         val = 1

#     print()




# 1 2 3 4 5 6 7 
#   1 2 3 4 5 
#     1 2 3 
#       1 

# n = int(input('n:'))

# for i in range(n ,0 ,-1):
#     val = 1

#     for j in range(n-i):

#         print(" ", end = " ")

#     for k in range(2*i - 1):

#         print(val, end=" ")
#         val +=1
    

   

#     print()




# A B C D E F G H I 
#   J K L M N O P 
#     Q R S T U 
#       V W X 
#         Y 

# n = int(input('n:'))
# val = ord('A')

# for i in range(n ,0 ,-1):
    
#     for j in range(n-i):

#         print(" ", end = " ")

#     for k in range(2*i - 1):

#         print(chr(val), end=" ")
#         val +=1
    

#     print()


#       A 
#     B C D 
#   E F G H I 
# J K L M N O P 

# n = int(input('n:'))
# val = ord('A')

# for i in range(n):
    
#     for j in range(n-i-1):

#         print(" ", end = " ")

#     for k in range(2*i - 1):

#         print(chr(val), end=" ")
#         val +=1
    

#     print()



# Z Y X W V U T 
#   S R Q P O 
#     N M L 
#       K 

# n = int(input('n:'))
# val = ord('Z')

# for i in range(n,0,-1):
    
#     for j in range(n-i):

#         print(" ", end = " ")

#     for k in range(2*i - 1):

#         print(chr(val), end=" ")
#         val -=1
    

#     print()



#         1 
#       * * * 
#     2 2 2 2 2 
#   * * * * * * * 

# n = int(input('n:'))
# val = 1

# for i in range(n):
    
#     for j in range(n-i-1):

#         print(" ", end = " ")

#     for k in range(2*i + 1):
         
#         if(i% 2 == 0):
#              print(val, end = " ")
#         else:
#              print("*" , end = " ")

#     if(i%2 == 0):
#         val +=1
    

#     print()




#       1 
#     * 2 * 
#   3 * 4 * 5 
# * 6 * 7 * 8 * 

# n = int(input('n:'))
# val = 1
# p = True

# for i in range(n):
    
#     for j in range(n-i-1):

#         print(" ", end = " ")

#     for k in range(2*i + 1):

#         if p:
#             print(val, end = " ")
#             val+=1
#             p = False
#         else:
#             print("*" , end = " ")
#             p = True

#     print()



#         1 
#       A B C 
#     2 2 2 2 2 
#   A B C D E F G 
# 3 3 3 3 3 3 3 3 3 

# n = int(input('n:'))
# val1 = 1


# for i in range(n):
#     val2 = ord('A')
#     for j in range(n-i-1):

#         print(" ", end = " ")

#     for k in range(2*i + 1):
        
#         if i % 2 == 0:
#             print(val1, end=" ")

#         else:
#             print(chr(val2), end = " ")
#             val2 += 1

#     if i% 2 == 0:
#         val1 += 1
#     print()



# 1 * 2 * 3 * 4 
#   * 5 * 6 * 
#     7 * 8 
#       * 

# n = int(input('n:'))
# val = 1
# p = True

# for i in range(n, 0 , -1):

#     for j in range(n-i):

#         print(" ", end = " ")

#     for k in range(2*i - 1):

#         if p:
#             print(val, end = " ")
#             val += 1
#             p = False
#         else:
#             print('*', end = " ")
#             p = True
 
      
#     print()


# A B C D E F G 
#   A B C D E 
#     A B C 
#       A 


# n = int(input('n:'))


# for i in range(n, 0 , -1):
#     val = ord('A')
#     for j in range(n-i):

#         print(" ", end = " ")

#     for k in range(2*i - 1):

#         print(chr(val) , end = " ")
#         val += 1
 
      
#     print()






# A A A A A A A 
#   B B B B B 
#     C C C 
#       D 


n = int(input('n:'))

val = ord('A')
for i in range(n, 0 , -1):
    
    for j in range(n-i):

        print(" ", end = " ")

    for k in range(2*i - 1):

        print(chr(val) , end = " ")
       
 
    val += 1   
    print()