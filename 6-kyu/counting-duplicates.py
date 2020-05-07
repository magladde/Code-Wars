def duplicate_count(text):
    chars = []
    text = text.lower()
    for i in text:
        if text.count(i) > 1:
            chars.append(i)
    chars = set(chars)
    return len(chars)

result = duplicate_count("abcda")
print(result)
