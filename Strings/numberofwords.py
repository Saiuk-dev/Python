text = "Hi my name is sai from pune"

words = text.split()

print("Total words:",len(words))

count = 0

for i in text.split():
    count += 1

print("Total words:",count)