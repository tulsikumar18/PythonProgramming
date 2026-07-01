# Display the count of substring present in the original string..


s1 = 'abcabcbbbccabcdabccccdab'

s2 = 'abc'

# Approach 1 : Use split mehtod and split the string where the pattern is present...the length/count will always be count - 1


i = 0 
j = len(s2) - 1

count = 0

print(s1.split('cd'))
s3 = s1.split(s2)

print(len(s3) - 1)



## Approach 2 : use loop and use slicing method..to check every 3rd character..


cnt = 0

for i in range(len(s1)):

    if s1[i : i + len(s2)] == s2:
        count += 1

print(count)
    


