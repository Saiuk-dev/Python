numbers = [10,20,30,40,50,60,70,80,90,100]

#Second Largest in List 
numbers.sort()
print("Second Largest", numbers[-2])

largest = float('-inf')
second_largest = float('-inf')

for i in numbers:
    if i>largest:
        second_largest = largest
        largest = i

    elif i>second_largest and i!=largest:
        second_largest = i

print("Second largest: ",second_largest)

##. Count even and odd numbers in a list

even = 0
odd = 0 

for i in numbers:
    if i%2 == 0:
        even += 1
    else:
        odd += 1

print("Even",even)
print("Odd",odd)

reverse= []

for i in numbers:
    reverse.insert(0,i)

print(reverse)