numbers = [10,15,20,25,30,35,40,42,47,52,53,54,56,58,96,89]
#. Count even and odd numbers in a list

even = 0
odd = 0

for i in numbers:
    if i%2 == 0:
        even += 1
    else:
        odd += 1

print(odd)
print(even)