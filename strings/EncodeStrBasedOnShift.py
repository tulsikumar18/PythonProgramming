# WAP TO encode given string , based on the shift value..


s2 ="I Love Progamming in Python"
s1 = "IronMan"

shift = int(input('Enter shift: '))
res = ""

for i in s2:

    if i == " ":
        res += " "
    else:

        res += chr(ord(i) + shift)

print(res)



