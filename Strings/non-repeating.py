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