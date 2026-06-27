n1 = int(input("n1: "))
n2 = int(input('n2: '))

# hcf = 1 # intially the hcf is 1 

# for i in range(1, min(n1,n2) + 1):

#     if n1 % i == 0 and n2 % i == 0:
#         hcf = i

# print(hcf)



# Approch 2 
# import math 

# res = math.gcd(n1,n2)
# print(res)




# Approach 3   # Ecludian method to find GCD

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD =", a)