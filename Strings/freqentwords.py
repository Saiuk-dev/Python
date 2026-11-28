text = "python is easy and python is powerful"

words = text.split()
frequency = {}

for i in words:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

most_frequent = max(frequency,key=frequency.get)
print("Most frequent word: ", most_frequent)
print("Frequency: ", frequency[most_frequent])