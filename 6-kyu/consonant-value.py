def solve(s):
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowels:
        s = s.replace(i, "_")
    calculate_val = s.split("_")
    scores = []
    for i in calculate_val:
        sum = 0
        if len(i) == 0:
            scores.append(-1)
        else:
            for j in i:
                val = ord(j)-96
                sum = sum + val
            scores.append(sum)
    return max(scores)

result = solve("zodiacs")
print(result)