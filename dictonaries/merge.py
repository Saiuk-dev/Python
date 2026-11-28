dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

result = {}

for i in dict1:
    result[i] = dict1[i]

for i in dict2:
    result[i] = dict2[i]

print(result)