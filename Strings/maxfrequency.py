text = "jai bajrangbali , my boss bajrangbali"
frequency = {}

for i in text.lower():
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

max_char = max(frequency,key=frequency.get)
print(max_char, frequency[max_char])

