

s1 = ['ate','tan','tea','eat','nat','bat','tab']


# output : [['ate','tea','eat'],['tan','nat'],['bat','tab']]



def string_sort(s):

    l1 = list(s)

    for i in range(len(l1)):

        for j in range(i+1,len(l1)):

            if l1[i] > l1[j]:

                l1[i],l1[j] = l1[j],l1[i]

    return "".join(l1)




d1 = {}


s1 = ['ate','tan','tea','eat','nat','bat','tab']

for i in s1 : 

    res = string_sort(i)

    if res not in d1:

        d1[i] = [i]
    else:

        d1[i].append(i)

    
print(d1)
    
        


            



