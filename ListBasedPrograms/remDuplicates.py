# l1 = [1,2, 3, 4, 1, 7, 8, 9, 10]


# out of place algorithm : using the different memory..

'''
if len(l1) > 0:

    res = []

    for i in l1:

        if i not in res:

            res.append(i)


    print(res)

    '''

# out of place method.. using the another list empty


'''
# approch 3:  Remove duplicates by replacing the duplicates by '#' and then remove the '#' from the l1
# O(n**2)

l1 = [1,2,1,3,4,2,7,8,7]
# o/p - [1,2,3,4,7,8]


i = 0
while i < len(l1):

    for j in range(i+1, len(l1)):

        if l1[i] == l1[j]:

            l1[j] = '#'

    i+=1

print(l1)

while '#' in l1:

    l1.remove('#')

print(l1)

'''