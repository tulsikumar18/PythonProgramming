
# insert the 2nd string, in the mid of first string...


s1 = 'virrat'
s2 = 'anushka'

# s1 = 'Uday'
# s2 = 'Bhavana'


res = ""

l = len(s1) // 2

# res += s1[:l] + s2 + s1[l:]

# print(res)



# Approach 2 : using loop


for i in range(l):
    
    res += s1[i]


res += s2

for i in range(l,len(s1)):

    res += s1[i]

print(res)





