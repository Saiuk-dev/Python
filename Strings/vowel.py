text = "Jai Bajrangbali , My boss Hanuman"

vowels = 0
consonants = 0

for i in str.lower():
    if i in "aeiou":
        vowels += 1

    elif i.isalpha():
        consonants += 1

print("Vowels: ", vowels)
print("consonants: ", consonants)