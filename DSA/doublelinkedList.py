class Node:

    def __init__(self, data):
        self.data = data 
        self.prev = None
        self.next = None


class double_Linked_list:

    def __init__(self):
        self.head = None


    def insert_at_first(self,data):

        newNode = Node(data)

        if self.head == None:

            self.head = newNode

        else:
            newNode.next = self.head
            self.head = newNode


    def delete_at_loc(self, loc):

        if loc <= 0:
            print('Enter location above zero')

        elif loc == 1:

            self.delete_at_first()

        elif loc > self.length():

            print('Enter the Location less than ->',self.length())

        elif loc == self.length():
            self.delete_at_last()

        else:

            temp = self.head
            cnt = 1

            while temp.next != None and cnt <= loc-1:
                temp = temp.next
                cnt += 1

            temp.next.next.prev = temp
            temp.next = temp.next.next
