def sum_vals(x):
    root = 0
    for i in str(x):
        root = root + int(i)
    return root

def digital_root(n):
    sum_val = sum_vals(n)
    while sum_val > 10:
        sum_val = sum_vals(sum_val)
    return sum_val

result = sum_vals(16)
print(result)