def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    return str(max(numbers)) + " " + str(min(numbers))

result = high_and_low("1 2 3 4 5")
print(result)