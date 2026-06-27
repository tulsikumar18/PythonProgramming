
# words Frequncy at particular index

s1 = "If you always do what you always did you will always get what you always got"

s2 = s1.split()

print(s2)

freq = {}


for i in range(len(s2)):

    ## convert it into lower

    char = s2[i].lower()

    if char not in freq:

        freq[char] = [i]

    else:
        freq[char] += [i]


for k, v in freq.items():

    print(k , '->', v)
    

    

