def is_divide_by(number, a, b):
    if (number % a == 0) & (number % b == 0):
        return True
    else:
        return False

result = is_divide_by(-12, 2, -6)
print(result)