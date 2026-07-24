## Implement the Linked List using the Stack..

class Node:

    def __init__(self , data):
        self.data = data
        self.addr = None


class stack_Linked_List:

    def __init__(self):
       self.head = None

    def push(self, val):
        newNode = Node(val)

        if self.head is None : 
            self.head = newNode

        else:
            newNode.addr = self.head 
            self.head = newNode

    def pop(self):

        if self.head is None:
            print("Stack Underflow")
            return None

        popped = self.head.data
        self.head = self.head.addr

        return popped
           
        
    def display(self):

        if self.head is None: 
            print('Nothing to display')

        else:
            temp = self.head

            while temp:

                print(temp.data , end = " -> ")
                temp = temp.addr



sll = stack_Linked_List()

sll.push('A')
sll.push('B')
sll.push('C')
sll.display()

print(sll.pop())

sll.display()

        