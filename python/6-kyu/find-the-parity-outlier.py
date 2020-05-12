def find_outlier(integers):
    counter = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            counter = counter + 1

    even_flag = False
    if counter > 1:
        even_flag = True

    if even_flag == True:
        for i in integers:
            if i % 2 != 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i

result = find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
print(result)