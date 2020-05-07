def is_pangram(s):
    letters = [x.lower() for x in s if x.isalpha()]
    letters = set(letters)
    if len(letters) < 26:
        return False
    else:
        return True

result = is_pangram("The quick, brown fox jumps over the lazy dog!")
print(result)