def ordered_count(inp):
    string_to_mod = inp
    result = []
    for i in inp:
        if i in string_to_mod:
            count = string_to_mod.count(i)
            result.append((i, count))
            string_to_mod = [x for x in string_to_mod if x != i]
    return result

result = ordered_count("abracadabra")
print(result)