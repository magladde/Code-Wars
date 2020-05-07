def twos_difference(lst):
    lst = sorted(lst)
    solutions = []
    for i in lst:
        for j in lst:
            if i - j == 2:
                solutions.append((min([i,j]), max([i, j])))
    return solutions

result = twos_difference([1, 2, 3, 4])
print(result)