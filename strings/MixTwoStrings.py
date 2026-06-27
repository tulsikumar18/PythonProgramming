### Accepts two strings..and mix the two strings.. as follows..


s1 = input('Enter s1 :')
s2 = input('Enter s2 : ')

res = ""

n1 = len(s1)
n2 = len(s2)


i = 0
j = len(s2) - 1

for i in range(max(len(s1),len(s2))):

    if i >= n1:
        res += s2[:n2-i]
        break
    elif j < 0:
        res += s1[i:]
        break

    else:
        res += s1[i]
        res += s2[j]
        i += 1
        j-=1

print(res)



    