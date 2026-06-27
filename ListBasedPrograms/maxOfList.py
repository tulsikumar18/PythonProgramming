l1 = [10,5,3,8,40,80,7]

# Without using inbuilt methods..

if len(l1) > 0:
    max = l1[0]

    for i in l1[1:]:

        if i > max:
            max = i

    print(max)