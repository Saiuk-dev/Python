numbers = [10,20,30,40,50,60,70,80,90,100]

max = max(numbers)
print(max)

tot = numbers[0]

for i in numbers:
    if i > tot:
        tot = i

print(tot)

#smallest element

smallest = numbers[0]

for i in numbers:
    if i<smallest:
        smallest = i 

print(smallest)

num1 = numbers[::-1]
print(num1)

reverse_list = []

for i in numbers:
    reverse_list.insert(0,i)

print(reverse_list)