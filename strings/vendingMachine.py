'''

create a class by the name vending machine and it should contains methods like add_items() , update_items()
display_items() , update_items(), total_bill()

when the obj is created an empty cart should be create automatically , and we need to pass dictionary items
# as follows..

'''


class Vending_Machine:

    all_products = {

        'bingo' : 20,
        'cola': 35,
        'oreo':30,
        'jimjam': 40,
        'dietcoke':60,
        'chikki' : 10,
        'redbull':200
    }

    def __init__(self):

        self.cart = {}

    def add_items(self, prod, qty):

        if prod in self.all_products:

            self.cart[prod] = qty
        else:

            print('The product is not available in the vending Machine')


    def display_items(self):

        if len(self.cart) != 0:

            print(self.cart)
        else :
            print('Cart is Empty')


    def update_items(self,prod, qty):

        if prod in self.cart:
            self.cart[prod] = qty

        else:
            print('the product is not present in the cart..')


    def total_bill(self):

        print('======= Total Bill Breakup ========')

        self.total_amnt = 0

        for self.k,self.v in self.cart.items():


            print(f'{self.k} : {self.v} * {self.all_products[self.k]} = ', self.v * self.all_products[self.k])

            self.total_amnt += self.v * self.all_products[self.k]

        print('Total Bill amount to be paid : ' , self.total_amnt)
        print('======== End of Bill ========')

        

obj = Vending_Machine()

obj.add_items('bingo',12)
obj.add_items('oreo',9)
obj.add_items('dietcoke',12)

obj.display_items()
obj.total_bill()

obj.update_items('dietcoke',20)
obj.display_items()
obj.total_bill()


