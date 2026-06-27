## Bubble sort is also known as Sinking Sort..

## compare the values , and swap if greater for ascending order..and vice versa..

## Best Case.. O(N) 
## Worst Case. O(n**2)

# It is a stable Algorithm...
# which means the 300(I) will come before only 300(II) , If it is before intially in the  unsorted



# time complexity is O(n**2) , has no real time use 

# l1 = [4,5,2,3,1,-100,300(I),300(II)]





l1 = [4,5,2,3,1,-100,300,300]

n = len(l1)

for i in range(n-1):

    for j in range(n-1-i): # In the next iteraration , the one elem gets already sorted so the i is included..
    

        if l1[j] > l1[j+1]:

            l1[j], l1[j+1] = l1[j+1], l1[j]

print(l1)

