t1 = "listen"
t2 = "silent"

if sorted(t1) == sorted(t2):
    print("Both the strings are anagrams")
else:
    print("Both are not anagrams")

#using dictionary and for loop 
frequency = {}

for i in t1:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

for i in t2:
    if i in frequency:
        frequency[i] -=1
    else:
        frequency[i] = -1

if all(value==0 for value in frequency.values()):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams ")