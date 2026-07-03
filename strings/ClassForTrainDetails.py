# WAP to design a functionality for railway department, create a class and it should contain 
## method like get_train() , get_train_total_seats() , get_train_for_theday() , total_collection

## accept the train details as follows:
#  




class Train_details:

    def __init__(self, train_info):

        self.train_info = train_info


    def get_train_name(self,train_no):

        ## Iterate the train_info and then find 
        for i in self.train_info:

            if i['train_no'] == train_no:

                print('The train name  is : ',i['train_name'])
                break
        else:
            print('The train is not available')


    def get_train_total_seats(self,train_no):

        total_seats = 0
        for i in self.train_info:

            if i['train_no'] == train_no:

                for seat_no in i['seats_available'].values():
                    total_seats += seat_no

        if total_seats != 0:

            return total_seats
        
        return 'The train is not available'



    def get_train_for_theday(self,day):

        res = []
        for train in self.train_info:
            
            if day.upper() in train['days_of_run']:

               res.append(train['train_name'])

        return res
    
    def total_collection(self, trainNo,**kwargs):


        total_amt = 0
        for train in self.train_info:

            if trainNo == train['train_no']:
               
               for k,v in kwargs.items():
                   
                   print(k ,":" , v ,'*', train['price'][k] , " = " , v *  train['price'][k] )
                   total_amt +=  v *  train['price'][k]

        print('The total and final bill paid is : ', total_amt)
                   
                   



## train information 

train_info = [
    
    {

    'train_no': 52319,
    'train_name': 'ChennaiExpress',
    'starting' : 'Banglore',
    'end' : 'chennai',
    'days_of_run' : ['MON','WED','FRI','SUN'],
    'seats_available':{'general': 250, 'sleeper' : 150 , 'ac' : 100},
    'price':{'general':250, 'sleeper':800,'ac':2000}

},
{

    'train_no': 52320,
    'train_name': 'RajdhaniExpress',
    'starting' : 'Delhi',
    'end' : 'Guwhati',
    'days_of_run' : ['TUE','WED','FRI','SAT'],
    'seats_available':{'general': 350, 'sleeper' : 300 , 'ac' : 250},
    'price':{'general':850, 'sleeper':1200,'ac':4500}

}]

obj = Train_details(train_info)

obj.get_train_name(52319)


print(obj.get_train_total_seats(52319))

print(obj.get_train_for_theday('WED'))


obj.total_collection(52320,general = 215,sleeper = 105,ac = 76)


