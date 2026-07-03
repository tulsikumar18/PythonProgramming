s2 = "aaaaaabbccccccdddeeefffffggghaaaabbb"

# output : a10b5c6d3e3f5g3h1


# Approach 1 : use dictionary...

res1 = ""

freq = {}


for i in range(len(s2)):

    if s2[i] not in freq:

        freq[s2[i]] = 1

    else:
        freq[s2[i]] += 1

    
for k,v in freq.items():

    res1 += k + str(v)

print(res1)




