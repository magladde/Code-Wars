def find_missing_letter(chars):
    counter = 0
    for i in chars:
        if chr(ord(i)+1) != chars[counter + 1]:
            return chr(ord(i)+1)
        counter = counter + 1

result = find_missing_letter(['a','b','c','d','f'])
print(result)