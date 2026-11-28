text = "Jai shree ram om sai ram my boss bajrangbali"
frequency = {}

for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

for i in frequency:
    if frequency[i] > 1:
        print(i, ":", frequency[i])