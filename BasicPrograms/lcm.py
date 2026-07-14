n1 = int(input("n1: "))
n2 = int(input('n2: '))


lcm = None
i = max(n1,n2) # lets assume intially the common factor will be the maximum of n1 and n2


Iter_count = 0

while True:

    Iter_count+=1
    
    if i % n1 == 0 and i % n2 == 0:
        lcm = i
        break

    i += max(n1, n2) # Here the next common value will be always the multiple of the max value so instead 
                    # incrementing by 1 increment by the max(n1, n2)

print(lcm)

print('Iter_count',Iter_count) # it shows the iteration count of the loop , how many times it has run





