numbers = [10,20,30,40,50,60,70,80,90,10,50,90,70,60,10,50,10,50,40,60,80,40,40,60,50,30,10,10,20,70]

frequency = {}

for i in numbers:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)


frequency1 = {}

for i in numbers:
    frequency1[i] = numbers.count(i)

print(frequency1)