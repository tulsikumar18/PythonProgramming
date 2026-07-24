
class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = next



class Circular_doubly_linked_list:

    def __init__(self):
        self.head = None


    def insert_at_last(self, val):

        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            newNode.prev = newNode

        else:

            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            newNode.prev = temp
            temp.next = newNode
            newNode.next = self.head
            self.head.prev = newNode

    def insert_at_first(self,val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            newNode.prev = newNode

        else:
            temp = self.head 
            while temp.next != self.head:
                temp = temp.next
            
            temp.next = newNode
            newNode.next = self.head
            newNode.prev = temp
            self.head.prev = newNode
            self.head = newNode


    def length(self):

        temp = self.head
        cnt = 1
        while temp:

            cnt += 1
            temp = temp.next
            if temp == self.head:
                break
        return cnt

    def insert_at_loc(self, val, loc):

        newNode = Node(val)

        if loc <= 0:
            print('Enter location above zero..')

        elif loc == 1:
            self.insert_at_first(val)

        elif loc == self.length()+1:
            self.insert_at_last(val)

        elif loc > self.length():
            print('Enter the location less than -> ', self.length())

        else:

            temp = self.head
            cnt = 1

            while cnt < loc-1:

                temp = temp.next
                cnt += 1

            newNode.next = temp.next
            temp.next.next.prev = newNode
            newNode.prev = temp
            temp.next = newNode

    def delete_at_first(self):

        if self.head is None:

            print('No nodes to delete...')

        elif self.length()  == 1:
            self.head = None

        else:

            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head.next.prev = temp
            self.head = self.head.prev


    def delete_at_last(self):

        if self.head is None:
            print('No nodes to delete...')

        elif self.length() == 1:
            self.head = None

        else:
            temp = self.head

            while temp.next.next != self.head:
                temp = temp.next

            temp.next = self.head
            self.head.prev = temp

    def delete_at_loc(self, loc):

        if loc <= 0:
            print('Enter location above zero..')
        
        elif loc == 1:
            self.delete_at_first()
     
        elif loc == self.length()+1:
            self.delete_at_last()
     
        elif loc > self.length():
            print('Enter the location less than -> ', self.length())
     
        else:
            pass



    def display_node_next_prev(self,node):

        pass

    

    def display(self):

        if self.head is None:

            print('No Nodes to display..')
        else:

            temp = self.head

            while temp:
                print(temp.data , end = ' <=> ')
                temp = temp.next

                if temp == self.head:
                    break

            print()


cdll = Circular_doubly_linked_list()

cdll.insert_at_first('A')
cdll.insert_at_first('AB')
cdll.insert_at_first('ABC')
cdll.insert_at_last('ABCD')

cdll.display()

cdll.delete_at_first()
cdll.display()

cdll.delete_at_first()
cdll.display()
