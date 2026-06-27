# WAP to display the frequency of each character in the given string...


s1 = "Supercalifragilisticexpalodicious"

freq = {}


for i in s1:

    if i not in freq:

        freq[i] = 1

    else:

        freq[i]+=1

## displaying the content of dictionary..


for k,v in freq.items():

    print(k ,"-", v)



