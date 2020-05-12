def camel_case(string):
    words = string.split()
    return_camel = ""
    for i in words:
        return_camel = return_camel + i.capitalize()
    return return_camel

result = camel_case("hello case")
print(result)