def cakes(recipe, available):
    if len(recipe) > len(available):
        return 0
    min_num = []
    for i in recipe:
        min_num.append(available[i]//recipe[i])
    return min(min_num)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
result = cakes(recipe, available)
print(result)