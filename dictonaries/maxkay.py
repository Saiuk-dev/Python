marks = {
    'Amit': 85,
    'Rahul': 92,
    'Sneha': 78,
    'Sai': 95
}

max_key = max(marks, key=marks.get)

print("Key with maximum value:", max_key)
print("Maximum value:", marks[max_key])