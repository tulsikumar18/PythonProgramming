##Display the key and value pair of unique word along with its count of vowels and count off consonents in the form of list..



## Approach 1 : use set to extract the unqiue keywords..then count the vowel and consonants , and the store it into dictionary..


s1 = "Once the most violent man called the one man the most violent"
s2 = s1.split()

s1 = list(set(s2))

# print(s1)

vowel = "AEIOUaeiou"

freq = {}

for i in s1:

    vow = 0
    const = 0

    for j in i :

        if j in vowel:
            vow += 1
        else:
            const += 1

    freq[i] = [vow,const]

    # or 

    # if freq[i] not in freq:

    #     freq[i] = [vow,const]


print(freq)



# Approch 2 : use the uniquness property of dictionary and push it there..instead of using set for it..