def dashatize(num):
    if num == None:
        return "None"
    num_string = str(num)
    if num_string[0] == "-":
        num_string = num_string[1:]
    return_val = ""
    for i in num_string:
        if int(i) % 2 == 1:
            return_val = return_val + "-" + str(i) + "-"
        else:
            return_val = return_val + i
    if return_val[0] == "-":
        return_val = return_val[1:]
    if return_val[-1] == "-":
        return_val = return_val[:-1]

    return_val = return_val.replace("--", "-")
    return return_val

result = dashatize(6815)
print(result)