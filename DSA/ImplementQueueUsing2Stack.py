

class STACK :

    def __init__(self):
       self.s1 = []

    def push(self, val):
        self.s1.append(val)

    def pop(self):
       
        if len(self.s1) == 0:
           return False
        else:
           return self.s1.pop()

    


class QUEUE:

    def __init__(self):
       self.InStack = STACK()
       self.OutStack = STACK()

    def enqueue(self, val):
        self.InStack.push(val)

    def dequeue(self):

        ## popped element from the one stack and pushed in other..
        
        while(len(self.InStack.s1) != 0):

            self.OutStack.push(self.InStack.pop())

        res = self.OutStack.pop()


        while len(self.OutStack.s1) != 0:
            self.InStack.push(self.OutStack.pop())

        return res

    def display(self):
       
        if len(self.InStack.s1) != 0:
            print(self.InStack.s1)
        else:
            print('Nothing to Display..')


    def peek(self):
        pass


q1 = QUEUE()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

q1.display()


print('RemovedElem is : ', q1.dequeue())
q1.display()