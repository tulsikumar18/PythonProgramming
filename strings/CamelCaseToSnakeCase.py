# Wap to convert the given camelcase to snake case string..


s1 = 'If You Are Good At Something Never Do It For Free'         # CamelCase


# output : if_you_are_good_at_something_never_do_it_for_free     # SnakeCase


res = ''

for i in s1:

    if ord(i)>= 65 and ord(i) <= 90:
        res += chr(ord(i) + 32)
    elif ord(i) >= 97 and ord(i) <= 122:
        res  += i
    else:
        res += "_"

print(res)




