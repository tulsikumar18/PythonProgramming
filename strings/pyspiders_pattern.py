


s1 = 'pyspiders'

# it will only work for the odd length..

# output ;
'''
        p         
        y         
        s         
        p         
p y s p i d e r s 
        d         
        e         
        r         
        s         
'''
  

n = len(s1)

if n%2 != 0:  # odd length...

    for i in range(n):

        for j in range(n):

            if i == n//2:
                print(s1[j], end = " ")

            elif j == n//2:
                print(s1[i], end = " ")
            
            else:
                print(" ", end = " ")

        print()



