def iq_test(numbers):
    number_list = numbers.split(" ")
    number_list = [int(i) for i in number_list]
    sum = 0
    for i in number_list:
        sum = sum + (i % 2)
    if sum > 1:
        for i in number_list:
            if i % 2 == 0:
                return number_list.index(i) + 1
    else:
        for i in number_list:
            if i % 2 == 1:
                return number_list.index(i) + 1

result = iq_test("2 4 7 8 10")
print(result)