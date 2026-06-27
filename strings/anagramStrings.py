# Wap to check the given strings are anagram strings are..

## Approch 1 : counting the fequency of each elements in both the strings.. and if dictionary are equal..
## they are anagrams...

# s1 = 'silent'
# s2 = 'listen'

'''
s1 = 'the-classroom'
s2 = 'school-master'


freq1 = {}

freq2 = {}


for i in s1:

    if i not in freq1:

        freq1[i] = 1

    else:

        freq1[i]+=1


## for string s2:
for i in s2:

    if i not in freq2:

        freq2[i] = 1

    else:

        freq2[i]+=1


if(freq2 == freq1):
    print('Anagram')
else:
    print('Not anagram')


'''

##Approach 2 : 

## use bubble sort..


def bubble_sort(s1):

    l1 = list(s1)
    for i in range(len(l1)):

        for j in range(i+1,len(l1)):

            if l1[i] > l1[j]:

                l1[i],l1[j] = l1[j],l1[i]
    
    return "".join(l1)


s1 = 'the-classroom'
s2 = 'school-master'


if bubble_sort(s1) == bubble_sort(s2):
    print('Anagram Strings')

else:
    print('Not an Anagram')



