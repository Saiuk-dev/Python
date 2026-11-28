numbers = [10, 20, 30, 40, 50]

search = 30
found = False

for i in numbers:
    if i == search:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")

if search in numbers:
    print("Element found")
else:
    print("Elemnt Not Found")