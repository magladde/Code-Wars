def find_missing_number(numbers):
    val = len(numbers) + 1
    max_sum = 0
    for i in range(val+1):
        max_sum = max_sum + i
    missing_sum = sum(numbers)
    return (max_sum - missing_sum)

result = find_missing_number([1,3,4])
print(result)