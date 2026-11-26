numbers = [10,20,30,40,50,60,70,80,90,100]

largest = float('-inf')
second_largest = float('-inf')

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i

    elif i>second_largest and i!=largest:
        second_largest = 1

print(second_largest)

numbers.sort()
print("Second largest:", numbers[-2])

