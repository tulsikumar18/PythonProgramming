
# # Approach 1 : using a list where each pairs are mentioned...

# def Convert_A_Z_B2Y_C2X(s1):

#     res = ''

#     char_pairs = [

#         ('A','Z'),
#         ('B','Y'),
#         ('C','X'),
#         ('D','W'),
#         ('E','V'),
#         ('F','U'),
#         ('G','T'),
#         ('H','S'),
#         ('I','R'),
#         ('J','Q'),
#         ('K','O'),
#         ('L','N'),
#         ('M','M'),
#         ('N','L'),
#         ('O','K'),
#         ('Q','J'),
#         ('R','I'),
#         ('S','H'),
#         ('T','G'),
#         ('U','F'),
#         ('V','E'),
#         ('W','D'),
#         ('X','C'),
#         ('Y','B'),
#         ('Z','A')
#     ]

    
#     for i in s1.upper():

#         for j, k in char_pairs:

#             if i == j:
#                 res += k
#     return res




# s1 = input('Enter the string: ')

# print(Convert_A_Z_B2Y_C2X(s1))






# Approach 2 : using ord function ...

def Convert_A_Z_B2Y_C2X(s1):

    res = ''

    for ch in s1.upper():

        diff = ord(ch) - ord('A')

        res += chr(ord('Z') - diff)

    return res




s1 = input('Enter the string: ')

print(Convert_A_Z_B2Y_C2X(s1))