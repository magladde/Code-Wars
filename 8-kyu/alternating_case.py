def to_alternating_case(string):
    return_string = ""
    for i in string:
        if i.islower() == True:
            return_string = return_string + i.upper()
        else:
            return_string = return_string + i.lower()
    return return_string

result = to_alternating_case("hello world")
print(result)