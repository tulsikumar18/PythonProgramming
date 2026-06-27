

## find the sum of prime number number in the list..


## Approach 1: 


def is_prime(num):


    if num == 1 : 
        return False
       
    for j in range(2, (num//2 )+1):

        if  num % j == 0:
            return False

    return True


sum = 0
l1 = [2,1,3,6,5,1,4]

for i in l1:
    if is_prime(i):
        sum+=i

print(sum)


