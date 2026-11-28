text = "cloudy weather is forecasted today"

frequency= {}

for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)
