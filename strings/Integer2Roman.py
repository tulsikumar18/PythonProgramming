# WAP to convert the given integer to roman number...
# the integer must be greater than one and less than 1000



# roman_pairs = {

#     1 : 'I',
#     4 : 'IV',
#     5 : 'V',
#     9 : 'IX',
#     10 : 'X',
#     40 : 'XL',
#     50 : 'L',
#     90 :'XC',
#     100 :'C',
#     400 : 'CD',
#     500 :'D',
#     900 :'CM',
#     1000:'M'
# }


roman_pairs = [
    (1 ,'I'),
    (4 ,'IV'),
    (5 ,'V'),
    (9 ,'IX'),
    (10,'X'),
    (40 ,'XL'),
    (50 , 'L'),
    (90 ,'XC'),
    (100 ,'C'),
    (400 , 'CD'),
    (500 ,'D'),
    (900 ,'CM'),
    (1000,'M')
]




def integer2Roman(num):

    res = ""

    if num >= 1 and num <= 1000:

        for val,rom in roman_pairs:

            while num >= val:
                res += rom
                num -= val

        return res
    else:

        return 'Enter number b/w 1 to 1000'
    


val = int(input('Enter the Value : '))

print(integer2Roman(val))

