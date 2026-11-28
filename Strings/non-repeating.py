text = "aabbccddeesffgghhkfjk"

frequency = {}

for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

for i in text:
    if frequency[i] == 1:
        print("First non-repeating character is: ",i)
        break

for i in text:
    if text.count(i) == 1:
        print("First non-repaeting character is: ",i)
        break

#for 2nd non repeating character 
count = 0
for i in text:
    if frequency[i] == 1:
        count += 1
        if count == 2:
            print("2nd Non repateing character is:" , i)
            break
