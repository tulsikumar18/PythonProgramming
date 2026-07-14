

s1 = ['ate','tan','tea','eat','nat','bat','tab']


# output : [['ate','tea','eat'],['tan','nat'],['bat','tab']]



s1 = ['ate', 'tan', 'tea', 'eat', 'nat', 'bat', 'tab']

def string_sort(s):

    l1 = list(s)

    for i in range(len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] > l1[j]:
                l1[i], l1[j] = l1[j], l1[i]

    return "".join(l1)


d1 = {}

for word in s1:

    key = string_sort(word)

    if key not in d1:
        d1[key] = [word]
    else:
        d1[key].append(word)

print(d1)
            







# Approch 2 : using sorted()

s1 = ['ate', 'tan', 'tea', 'eat', 'nat', 'bat', 'tab']

d = {}

for word in s1:
    key = "".join(sorted(word))

    if key not in d:
        d[key] = [word]
    else:
        d[key].append(word)

print(list(d.values()))