# WAP to create functionality for flight management , it should contains methods like , 
# generate tickets(), and get total cost..., book ticket()


# generate tickets..
#  1 has to be present
# frist 3 char from airlines name, 
# first 3 char from starting,
# 5 digits random numbers..
# first 3 chars from dest..

import numpy as np


class flight:

    def __init__(self,flight_details):
        self.flight_details = flight_details
        
        
    def generate_tickets(self, flightid, total_tickets):

       
        for flight in self.flight_details:

            if flight['flightid'] == flightid:
                
                for j in range(total_tickets):
                    res = ''
                    res += '1' + flight['flightname'][:3].upper() + flight['starting'][:3].upper() + str(np.random.randint(11111,99999)) + flight['destination'][:3].upper()
                    print(res)
                break
        else:
            print('No flight available')
        
        self.get_total_cost(flightid,total_tickets)


        


    def get_total_cost(self,flightid,total_tickets):

        print('======Total Cost ======')

        total_amt = 0

        for flight in self.flight_details:

            if flight['flightid'] == flightid:

               total_amt += flight['price'] * total_tickets

        total_amt += 0.02 *  0.065
       
        print('Total amount to be paid is : ' , total_amt)
        print('======End of Cost=====')

    

    def book_tickets(self,flightid,total_tickets):

        for flight in self.flight_details:

            if flight['flightid'] == flightid:
                
                flight['avail_seats'] -= total_tickets
                print(flight)
                break

        else:

            print('Flight not available only')




flight_details = [{

    'flightid' : '1ABC234',
    'flightname':'Air India',
    'starting' : 'Banglore',
    'destination' : 'Dubai',
    'total_seats' : 250,
    'avail_seats': 200,
    'price' : 22500
},

{

    'flightid' : '1XYZ234',
    'flightname':'Indigo',
    'starting' : 'Kolkata',
    'destination' : 'Bangkok',
    'total_seats' : 225,
    'avail_seats': 215,
    'price' : 21500
},
{

    'flightid' : '1CDE234',
    'flightname':'SpiceJet',
    'starting' : 'Guwahati',
    'destination' : 'Delhi',
    'total_seats' : 222,
    'avail_seats': 120 ,
    'price' : 7900
}]


obj = flight(flight_details)

obj.generate_tickets('1CDE234', 5)

obj.book_tickets('1CDE234', 5)




