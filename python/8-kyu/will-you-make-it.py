def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance_able_to_travel = mpg * fuel_left
    if distance_able_to_travel >= distance_to_pump:
        return True
    else:
        return False

result = zero_fuel(50, 25, 2)
print(result)