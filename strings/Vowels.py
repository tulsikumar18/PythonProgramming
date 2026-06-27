
## Count the number of vowels and number of consonants..

## when it is space (' ') , it should not be counted in any of these..v and c , we can write cont



s1 = 'Python coding is Awesome'
v = 0
c = 0

for i in s1:

    if i  in 'aeiouAEIOU':
        v+=1
    elif i not in 'aeiouAEIOU':
        c+=1
    else:
        continue


print(f'Vowel is {v} and consonant is {c}')
