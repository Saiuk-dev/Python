text = "jai shree ram "

vowels = 0
consonants = 0

for i in text.lower():
    if i in "aeiou":
        vowels += 1

    elif i.isalpha():
        consonants += 1

print("Vowels: ", vowels)
print("consonants: ", consonants)