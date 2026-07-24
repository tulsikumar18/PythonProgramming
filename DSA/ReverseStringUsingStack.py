## REVERSE THE STRING USING THE STACK ..


class stack:

    def __init__(self):
        self.s1 = []


    def push(self, val):
        self.s1.append(val)

    def pop(self):

        if len(self.s1) == 0:
            return False
        else:
            return self.s1.pop()
        
    def display(self):
       
        if len(self.InStack.s1) != 0:
            print(self.InStack.s1)
        else:
            print('Nothing to Display..')


stk = stack()

str1 = input('Enter the string..:')

res = ''

for char in str1:
    stk.push(char)

while len(stk.s1) != 0:
    res += stk.pop()

print('Reversed string is :', res)


