def in_array(array1, array2):
    return_array = []
    for sub_string in array1:
        for word in array2:
            if sub_string in word:
                return_array.append(sub_string)
                break
    return_array = sorted(list(set(return_array)))
    return return_array

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
result = in_array(a1, a2)
print(result)