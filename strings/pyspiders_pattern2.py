
## WAP to display the  

'''

     P
  Y S P 
 I D E R S
P Y S P I D E



'''

s2 = "PYSPIDERS"

row = int(input('Enter the no or rows..: '))


for i in range(row):

   for j in range(len(s2)):
    
      print(" " * (row-1 - i) , s2[j] * (2*i + 1))






