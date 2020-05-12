def find_it(seq):
    unique_values = list(set((seq)))
    unique_count = [seq.count(x) for x in unique_values]
    dictionary = zip(unique_values, unique_count)
    odd_int = {val : count for val, count in dictionary if count % 2 == 1}
    key = odd_int.keys()
    key_list = list(key)
    answer = key_list[0]
    return answer

result = find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
print(result)