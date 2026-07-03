

# encode the morse code..

d1 = {

    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' :'-....',
    '7' :'--...',
    '8' :'---..',
    '9' :'----.'
}

'''
### Encode the values..

def encode_number(d1, val):

    res = ""
    for i in val:

        res += d1[i]

    return res


val = input('Enter the value : ')

print(encode_number(d1,val))



'''

### Decode the string...

# change the keys to values and then values to keys..in the dictionary...

# d2 = {}

# for k,v in d1.items():

#     d2[v] = k

# print(d2)

## OR

## instead of this we can use the dict comprehension ..

d2 = {val : key for key,val in d1.items()}

print(d2)

'''

def decode_morse(d2, code):

    res = ""

    ## split the code wherever the space is present such that ..every 5 chaacters we can get..


    morse_cde = code.split()

    for i in morse_cde:

    ## I'll check every character in the d2 and then if found i'll concatenate that to res...

        if i in d2:

            res += d2[i]
        else:

            return 'Invalid Morse code..'

    return res


print('Enter the morse code with 5 characters only and then give one space b/w every 5 characters...: ')

morse_code = input('Enter the morse Code : ')

print(decode_morse(d2,morse_code))


'''

## Approach 2 : use matchcase...



def decode_morse(d2, code):

    res = ""

    morse_cde = code.split()

    for i in morse_cde:

        match(i):

            case '-----' : res += '0'

            case '.----' : res += '1'

            case '..---' : res += '2'

            case "...--" : res += "3"

            case "....-" : res += "4"

            case "....." : res += "5"
            case "-....": res += "6"
            case "--..." : res += "7"
            case "---.." : 	res += "8"

            case "----." : res += "9"

    return res


print('Enter the morse code with 5 characters only and then give one space b/w every 5 characters...: ')

morse_code = input('Enter the morse Code : ')

print(decode_morse(d2,morse_code))


