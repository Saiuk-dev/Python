numbers = [7,7,5,5,8,9,8,5,6,2,3,5,4,8,5,2,2,3,5,6,9,8,5,4,7,5,6,9,8]

unique_list = []

for i in numbers:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)

u1 = list(set(numbers))
print(u1)

u2 = list(dict.fromkeys(numbers))
print(u2)