
# Create a class , it should have mathod like additems(), display() and update_items  / delete items, 
# and then when the object is created an empty dictionary automatically created and performs all the 
# above method on that dictionary without using inbuilt methods..




class dict_operation:

    def __init__(self):
        self.d1 = {}

    def add_items(self,k,v):

        if k not in self.d1:

            self.d1[k] = v
        else: 
            print('Key already Exists..')



    def display(self):
        
        print(self.d1)

    def update_items(self, k , v):
        
        if k in self.d1:

            self.d1[k] = v
        else:
            print('the key doesnt exist: ')

    def delete_items(self, k):

        if k in self.d1:
            del self.d1[k]

        # del keyword is used to delete the elements from the dictionary...

        else:
            print('Key not exists.')

obj = dict_operation()

obj.add_items('one', 10)
obj.add_items('two', 20)
obj.add_items('three',40)

obj.display()

obj.update_items('three',30)

obj.delete_items('two')

obj.display()

obj.update_items('four',50) # the key doesnt exist: 