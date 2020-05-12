def solution(digits):
    largest_num = 0
    for i in range(len(digits)):
        five_digit_num = int(digits[i:(i+5)])
        if five_digit_num > largest_num:
            largest_num = five_digit_num
    return largest_num

result = solution("1234567890")
print(result)