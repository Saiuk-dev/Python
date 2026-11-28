#count frequency of each character in a string 
text = "banana"
frequency = {}

for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)