def count(string):
    characters = set(string)
    return_dict = {}
    for i in characters:
        num = string.count(i)
        return_dict.update({i:num})
    return return_dict

result = count("aba")
print(result)