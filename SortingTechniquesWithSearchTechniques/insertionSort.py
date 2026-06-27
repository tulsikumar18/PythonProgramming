
## It is sorting algorithm...where we find the relevant index of the key and then insert it there..
## To find the relevant index or position ,where we have to insert it , we will shift the values toward the 
## right till I get the relevant index of the key..

# Best Case.. O(n)

l1 = [23,1,10,5,2]

for i in range (len(l1)):

    key = l1[i]
    index = i-1

    while key < l1[index] and index >= 0:

        ## reduce the index till the values are less and then 

        ## shift toward the right to make space for the key..

        l1[index+1] = l1[index]
        index -= 1

    l1[index+1] = key

print(l1)

