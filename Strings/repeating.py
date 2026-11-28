text = "programming"

freqency = {}

for i in text:
    if i in freqency:
        print("First Repaeating chracter is: ",i)
        break
    else:
        freqency[i] = 1


seen = set()

for i in text:
    if i in seen:
        print("first repeating character is: ",i)
        break
    else:
        seen.add(i)