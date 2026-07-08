# Digital Sum : The super digit of a number is obtained by repeatedly adding its digits until 
# only one digit remains.

n = int(input('Enter the number: '))

res = 0


while n >= 10:
    str_val = str(n)
    for i in range(len(str_val)):

        res += int(str_val[i])
    n = res
    res = 0

print(n, end=" ")

   
   



    