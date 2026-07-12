
class Circular_queue:

    def __init__(self,maxSize):
        
        self.maxSize = maxSize
        self.cq = [None] * self.maxSize
        self.front = -1
        self.rear = -1


    def isFull(self):
        if (self.front == 0 and self.rear + 1 == self.maxSize) or (self.rear + 1 == self.front):
            return True
        else:
            return False
        
    def isEmpty(self):

        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False


    def enqueue(self, val):
        if self.isFull():
            print("Circular Queue is full")
        
        # if first Elem is to be enqueued..
        if self.front == -1:
            self.front = 0

        #Increment the Rear and the assign the value..
        self.rear = (self.rear + 1) % self.maxSize
        self.cq[self.rear] = val


    def dequeue(self):

        if self.isEmpty():
            print('Circular Queue is Empty')
        
        else:
            # store the id of the front 
            idx = self.front

            # if it has only one Element.. then assign front and rear to -1 and before that change the 
            # value at front & rear to None as , if not assigned none , list will default shift towards left.
            if self.front == self.rear: 
                self.front = -1 
                self.rear = -1 

            # increment the front and change the value to None
            else:
                self.front = (self.front + 1) % self.maxSize
            self.cq[idx] = None

    def search_char_by_shift(self, char ,shift):

        if self.isEmpty():
            print('Circular queue is Empty')
        
        # If only one Elem is present..
        if char in self.cq:
        
            if self.front == self.rear:
                return self.cq[self.front]
        
            else:

                # Find out the Index of the char and then shift by using % maxSize..
                index1 = self.cq.index(char)
                index1 = (index1 + shift) % self.maxSize
                return self.cq[index1]
        else: 
            return char


    def display(self):

        if self.isEmpty():
            print('Circular Queue is Empty..')
        else:
            print(self.cq)

        


## Take input from the user...
n = int(input('Enter the length of string : '))

q1 = Circular_queue(n)

for i in range(n):

    char = input('Enter char : ')
    q1.enqueue(char)


q1.display()

s1 = 'pyspiders'
res = ''

for i in s1:

    res += q1.search_char_by_shift(i,4)

print()
print(res)

        