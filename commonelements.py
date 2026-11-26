list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print(common)

#if Order Does not matters 
c2 = list(set(list1) & set(list2))
print(c2)