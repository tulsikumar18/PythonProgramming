
from posixpath import sep
l1 = [1, 2, 3, 2, 3, 1, 0]

# remove duplicates without set..list

#approch 1 using set

# l1 = list(set(l1))
# print(l1)




dict = {

    'One': 12,
    'Two': 23,
    'Three': 34,
    'Four': 45
}


#find the key with max value


# max_value = max(dict.values())

# print(max_value)




# for k, v in dict.items():

#     if(v == max(dict.values())):
#         print(k)



# Inverting the dictionary..
# inv = {}

# for k,v in dict.items():

#     inv[v] = k

# print(inv)





# l = ["apple", "ant", "banana", "bat", "cat"]

# group = {}

# for word in l:

#     key = word[0]

#     if key not in group:

#         group[key] = []

#     group[key].append(word)

# print(group)


    



# print(dict.fromkeys(l1,[1,2,3]))
# print(dict.get('t'))
# print(dict.pop('One'))

# for key, value in dict.items():
#     print(key, value)


# for values in dict.values():
#     print(values)



# str = 'programmings'
# freq = {}

# for ch in str:

#     if(ch in freq):

#         freq[ch] +=1
#     else:
        
#         freq[ch] = 1

# print(freq)



# string 

str = 'we-are-the-students'

res = str.split(sep  = 'we')
print(res)

