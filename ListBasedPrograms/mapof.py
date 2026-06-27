# take string as input 1 2 3 4 5 and then return list [1, 2, 3, 4, 5]


# Approach 1 : taking input in the string form and then use str.split function 

'''
s = '1 2 3 4 5'

l1 = s.split() # by default it splits in the space..

print(l1)      #['1', '2', '3', '4', '5']

res=[]

for i in l1:
    res.append(int(i))

print(res) #[1, 2, 3, 4, 5]



# Approach 2 : using map function 
# syntax of map 
        # map(function , iterable) -> map object


l1 = ['1', '2','3','4','5']
res = map(int,l1)
print(res)
print(set(res))     #[1, 2, 3, 4, 5]

'''


'''
### Approach 3:  Here the input is taken as string and then every input is converted into int function
### and then  convert it into list

n = int(input('n: '))

l1 = list(map(int,input().split()))[:n]

print(l1)


output : 
n: 5
1 2 3 4 5 6 7 8
[1, 2, 3, 4, 5]




finding cube using the lambda function 
lambda is an anonymous function , without def keyword..





l1 = [1,2,3,4, 5]

res = map(lambda n: n**3, l1)

print(list(res))    # [1, 8, 27, 64, 125]

'''



# n = int(input('n: '))

# l1 = list(map(int,input().split()))[:n]

# print(l1)


