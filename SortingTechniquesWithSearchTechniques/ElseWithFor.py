### when the loop excutes completely.. without break then  only the else block gets executed..

n = int(input('Enter the val: '))

for i in range(1, 11):

    if i == n: 
        break
else:

    print('Loop Executed Completely..')