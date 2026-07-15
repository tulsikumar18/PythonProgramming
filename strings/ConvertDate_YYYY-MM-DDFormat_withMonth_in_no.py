''' 
Convert the date into the format YYYY-MM-DD.

Input: 19-Jun-1972
Output: 1972-06-19

'''


# def ConvertDateMonth_in_no(s1):

#     res = ''

#     month = [
#         ('jan' , '01'),
#         ('feb' , '02'),
#         ('mar' , '03'),
#         ('apr' , '04'),
#         ('may' , '05'),
#         ('jun' , '06'),
#         ('jul' , '07'),
#         ('aug' , '08'),
#         ('sep' , '09'),
#         ('oct' , '10'),
#         ('nov' , '11'),
#         ('dec' , '12')
#     ]

#     l1 = s1.split('-')

#     mon = l1[1]

#     res += l1[2] + '-'

#     for x,y in month:
#         if mon.lower() == x:
#             res += y + '-'
#             break

#     res += l1[0]

#     return res


# s1 = input('Enter the date: ')

# print(ConvertDateMonth_in_no(s1))


# Approach 2 : using dictionary..


def ConvertDateMonth_in_no(s1):

    res = ''

    month = {
       
       'jan': '01', 'feb' : '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun':'06', 'jul' : '07',
       'aug':'08', 'sep':'09','oct':'10','nov': '11', 'dec': '12'
    }

    date, mon, year = s1.split('-')

    # if int(date) > 31:
    #     print('Enter date lesser than equals to 31')
    #     exit()

    res += year + '-'

    if mon.lower() in month:
        res += month[mon.lower()] + '-'
    
    res += date

    return res


s1 = input('Enter the date: ')

print(ConvertDateMonth_in_no(s1))